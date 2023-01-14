# postseam-example-python-server

Backend application for Postseam's example app.

## Background

As part of Postseam's
[How to Build Saas Applications](https://blog.postseam.com/tag/how-to-build-saas-applications/) series, we will be
creating a basic ecommerce application. This repository contains Postseam's example gRPC server implemented in Python. This application will be used develop our backend services and serve our front end application.

## Setup

Create a Python virtual environment

```bash
python -m virtualenv venv
```

Activate environment

```bash
. venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

## Running the server

To run the server in the docker container (preferred) executing the following command:

```bash
make build_local && run_local

```

The server can be run locally by executing the following command:

```bash
python main.py

```
