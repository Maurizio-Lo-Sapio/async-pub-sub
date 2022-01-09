# syntax=docker/dockerfile:1
FROM python:3.7-alpine
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . .
COPY config.json config.json
COPY greetings_pb2.py greetings_pb2.py
CMD ["flask", "run", "--eager-loading", "--port",  "5001"]

