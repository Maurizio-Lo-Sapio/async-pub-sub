# syntax=docker/dockerfile:1
FROM python:3.7-alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
COPY config.json config.json
COPY greetings_pb2.py greetings_pb2.py
CMD [ "python", "./consumer.py" ]

