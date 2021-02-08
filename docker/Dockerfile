FROM python:3.7

# Install tini and create an unprivileged user
ADD https://github.com/krallin/tini/releases/download/v0.19.0/tini /sbin/tini
RUN addgroup --gid 1001 "elg" && \
      adduser --disabled-password --gecos "ELG User,,," \
      --home /elg --ingroup elg --uid 1001 elg && \
      chmod +x /sbin/tini

# Copy in our app, its requirements file and the entrypoint script
COPY requirements.txt /elg/

# Everything from here down runs as the unprivileged user account
USER elg:elg

WORKDIR /elg

# Create a Python virtual environment for the dependencies
RUN python -mvenv venv && venv/bin/pip --no-cache-dir install -r requirements.txt

ARG MODEL_DIR
COPY models/$MODEL_DIR /elg/models/cloud

COPY docker/toxic_classifier.py /elg/toxic_classifier.py
COPY docker/elg_app.py docker/docker-entrypoint.sh /elg/

ARG ANNOTATION_TYPE
ENV WORKERS=1 REQUEST_SIZE_LIMIT=100000 ANNOTATION_TYPE=$ANNOTATION_TYPE

ENTRYPOINT ["./docker-entrypoint.sh"]
