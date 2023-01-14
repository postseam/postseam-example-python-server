FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install make

EXPOSE 8000
CMD [ "python", "main.py"]
