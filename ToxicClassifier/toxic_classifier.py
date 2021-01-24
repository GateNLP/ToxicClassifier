from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import sklearn
import sys
from scipy.special import softmax

class ToxicClassifier():

    def __init__(self, model, lang, gpu):

        self.model = ClassificationModel(
                "roberta", "../models/"+lang+"/"+model, use_cuda=gpu
        )

    def classify(self, text):
         test_predictions, raw_outputs = self.model.predict([text])
         probabilities = list(softmax(raw_outputs[0])[0])
         return test_predictions[0], probabilities

