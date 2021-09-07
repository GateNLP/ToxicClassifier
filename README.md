# ToxicClassifier

Toxic Classifiers developed for the GATE Cloud. Two models are available:
- kaggle: trained on the [Kaggle Toxic Comments Challenge dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/overview).
- olid: trained on the [OLIDv1 dataset from OffensEval 2019](https://sites.google.com/site/offensevalsharedtask/olid).

We fine-tuned a `Roberta-base` model using the [`simpletransformers`](https://simpletransformers.ai/) toolkit.


## Requirements
`python=3.8`
`pandas`
`tqdm`
`pytorch`
`simpletransformers`

## Pre-defined environments

conda

`conda env create -f environment.yml`

pip

`pip install -r requirements.txt`

(if the above does not work or if you want to use GPUs, you can try to follow the installation steps of `simpletransformers`: [https://simpletransformers.ai/docs/installation/](https://simpletransformers.ai/docs/installation/)

## Models

1. Download models from [the latest release of this repository](https://github.com/GateNLP/ToxicClassifier/releases/latest) (currently available `kaggle.tar.gz`, `olid.tar.gz`)
2. Decompress file inside `models/en/`

## Basic Usage

`python __main__.py -t "This is a test"` (should return 0 = non-toxic)

`python __main__.py -t "Bastard!"` (should return 1 = toxic)

## Options
- `t`: text
- `l`: language (currently only supports "en")
- `c`: classifier (currently supports "kaggle" and "olid" -- default="kaggle")
- `g`: gpu (default=False)

## Output
The output is composed by the predicted class and the probabilities of each class. 

## REST Service
Pre-built Docker images are available for a REST service that accepts text and returns a classification according to the relevant model - see the "packages" section for more details.
