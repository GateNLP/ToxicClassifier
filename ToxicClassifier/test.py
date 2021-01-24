import sys
import argparse
from toxic_classifier import ToxicClassifier
import pandas as pd
import time



#Load config: 

parser = argparse.ArgumentParser(description='GATE Toxic Classifier: test with large test sets.')
parser.add_argument('-f', help='input file (csv format)')
parser.add_argument('-l', help='language', choices=['en'], default='en')
parser.add_argument('-c', help='classifier', choices=['kaggle'], default='kaggle')
parser.add_argument('-g', help='gpu', type=bool, choices=[True, False], default=False)

args = parser.parse_args()

v_args = vars(args)

f = v_args['f']

l = v_args['l']

g = v_args['g']

classifier = ToxicClassifier(v_args['c'], l, g)

df = pd.read_csv(f)

start = time.time()
for t in df['comment_text']: 
    print(classifier.classify([t]))
end = time.time()
print(end - start)
