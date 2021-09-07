# Building Docker images and GATE Cloud apps

The toxic and offensive classifiers are deployed on GATE Cloud via a two step process, first the classifier itself is deployed as a container that exposes an ELG-compliant API endpoint using the Quart python HTTP framework, then the GATE Cloud API endpoint is a simple GATE app that contains an ELG client PR configured to call the Python endpoint.  The ELG-compliant images are also published directly on the ELG platform.

## Building the Python classifier images

The Python-based classifiers for toxic (kaggle dataset) and offensive (olid dataset) language can be built using the `./build.sh` script in this directory.  The relevant model files must be downloaded and unpacked in `../models` as described in [the main README](../README.md).  The images are pushed to the GitHub container registry:

```
TAG=ghcr.io/gatenlp/toxicclassifier/toxic-classifier:latest ./build.sh en/kaggle Toxic
TAG=ghcr.io/gatenlp/toxicclassifier/offensive-classifier:latest ./build.sh en/olid Offensive
```

The `Dockerfile` has been designed so that the two images will share most of their layers including the (large) Python virtual environment, only the model layer and configuration variables will differ.

## Building the GATE Cloud applications

The GATE applications that call these Python endpoints can be created using the `build_zip.sh` script in the `cloud-applications` folder:

```
cd cloud-applications
./build_zip.sh metadata/toxic http://<deployed-location-of-toxic-classifier>:<port>/process toxic.zip
./build_zip.sh metadata/offensive http://<deployed-location-of-offensive-classifier>:<port>/process offensive.zip
```

This will create zip files with the appropriate `application.xgapp`, `metadata` and the ELG client plugin, which can then be published as services in the normal way.
