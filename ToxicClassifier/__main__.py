import sys
import argparse
from toxic_classifier import ToxicClassifier


#Load config: 

parser = argparse.ArgumentParser(description='GATE Toxic Classifier.')
parser.add_argument('-l', help='language', choices=['en'], default='en')
parser.add_argument('-t', help='text to be classified')
parser.add_argument('-c', help='classifier', choices=['kaggle', 'olid'], default='kaggle')
parser.add_argument('-g', help='gpu', type=bool, choices=[True, False], default=False)

args = parser.parse_args()

v_args = vars(args)

text = v_args['t']

l = v_args['l']

g = v_args['g']

classifier = ToxicClassifier(v_args['c'], l, g)



print(classifier.classify(text))
