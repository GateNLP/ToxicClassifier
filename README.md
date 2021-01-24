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

(if the above does not work, you can try to follow the installation steps of `simpletransformers': [https://simpletransformers.ai/docs/installation/](https://simpletransformers.ai/docs/installation/).

