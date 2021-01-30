from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import sklearn
import sys
from scipy.special import softmax

# approach used here comes from this simpletransformers issue that reported the same problem
# https://github.com/ThilinaRajapakse/simpletransformers/issues/761

model = None

def get_model():
    global model
    if model is None:
        model_args = {"use_multiprocessing": False, "silent": True}
        model = ClassificationModel('roberta', 'models/cloud', use_cuda=False, args=model_args)
    return model

def classify(text):
     test_predictions, raw_outputs = get_model().predict([text])
     probabilities = list(softmax(raw_outputs[0])[0])
     return test_predictions[0], probabilities

