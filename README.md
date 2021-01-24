# ToxicClassifier

Toxic Classifier trained on the [Kaggle Toxic Comments Challenge dataset] (https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/overview).

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

1. Download models from `gateservice8:/export/data/carolina/ToxicClassifier/models/en/` (currently available `kaggle.tar.gz`)
2. Decompress file inside `models/en/`

## Basic Usage

`python __main__.py -t "This is a test"` (should return 0 = non-toxic)

`python __main__.py -t "Bastard!"` (should return 1 = toxic)

## Options
`t`: text
`l`: language (currently only supports "en")
`c`: classifier (currently only supports "kaggle")
`g`: gpu (default=False)

