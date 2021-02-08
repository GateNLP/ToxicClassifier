#!/usr/bin/env python3
#
#    Copyright 2020 European Language Grid
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
# Very simple-minded whitespace tokeniser that returns a Token annotation for
# every sequence of non-whitespace characters in the supplied text.
#

from quart import Quart, request
from quart.exceptions import BadRequest
from quart.utils import run_sync
import cgi
import codecs
import os

import collections
import json
import re
import warnings

import os

from toxic_classifier import classify

annotationType = os.environ['ANNOTATION_TYPE']

app = Quart(__name__)
app.config["JSON_SORT_KEYS"] = False

# Take plain text post size limit from env
size_limit = int(os.environ.get('REQUEST_SIZE_LIMIT', 50000))

class RequestTooLarge(Exception):
    pass

def invalid_request_error(e):
    """Generates a valid ELG "failure" response if the request cannot be parsed"""
    return {'failure':{ 'errors': [
        { 'code':'elg.request.invalid', 'text':'Invalid request message' }
    ] } }, 400

app.register_error_handler(BadRequest, invalid_request_error)
app.register_error_handler(UnicodeError, invalid_request_error)

@app.errorhandler(RequestTooLarge)
def request_too_large(e):
    """Generates a valid ELG "failure" response if the request is too large"""
    return {'failure':{ 'errors': [
        { 'code':'elg.request.too.large', 'text':'Request size too large' }
    ] } }, 400

async def get_text_content(request, charset):
    decoder_factory = codecs.getincrementaldecoder(charset)
    decoder = decoder_factory(errors='strict')
    content = ''
    limit_hit = False
    async for chunk in request.body:
        if not(limit_hit):
            content += decoder.decode(chunk)
        if len(content) > size_limit:
            limit_hit = True
    if limit_hit:
        raise RequestTooLarge()

    content += decoder.decode(b'', True)
    return content

@app.route('/process', methods=['POST'])
async def process_request():
    """Main request processing logic - accepts a JSON request and returns a JSON response."""
    ctype, type_params = cgi.parse_header(request.content_type)
    if ctype == 'text/plain':
        content = await get_text_content(request, type_params.get('charset', 'utf-8'))
    elif ctype == 'application/json':
        data = await request.get_json()
        # sanity checks on the request message
        if (data.get('type') != 'text') or ('content' not in data):
            raise BadRequest()
        content = data['content']
    else:
        raise BadRequest()

    annotations = dict()

    prediction, probabilities = await run_sync(classify)(content)

    features = dict()

    features["is"+annotationType] = prediction == 1
    features["probability"] = probabilities[prediction]

    annot = {"start": 0, "end": len(content), "features": features}

    annotations.setdefault(annotationType+"Language", []).append(annot)

    return dict(response = { 'type':'annotations', 'annotations':annotations  })

if __name__ == '__main__':
    app.run()
