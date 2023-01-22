# postseam-example-python-server

Backend application for Postseam's example app.

## Background

As part of Postseam's
[How to Build Saas Applications](https://blog.postseam.com/tag/how-to-build-saas-applications/) series, we will be
creating a basic ecommerce application. This repository contains Postseam's example gRPC server implemented in Python. This application will be used develop our backend services and serve our front end application.

## Setup

Create a Python virtual environment:

```bash
python -m virtualenv venv
```

Activate environment:

```bash
. venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run tests locally:

```bash
make unit_test
```

[Optional] Run tests in the container:

```bash
make test_docker
```

## Running the server

You'll need to start a local instance of Postgres and the backend server to get the application working correctly. The following command will help you get setup.

### Postgres setup

Download the official Postgres image:

```bash
docker pull postgres:15.1
```

Run the image:

```bash
make postgres_docker
```

### Server setup

To run the server in the docker container (preferred) executing the following command.
Note, the following command builds the image and connects
it with the Postgres image we started above.

```bash
make build_docker && make run_docker

```

The server can also be run without Docker by executing the following command:

```bash
python main.py

```
