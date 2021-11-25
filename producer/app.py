from flask import Flask, render_template, request
import pika
import time
import json
import greetings_pb2

connected = False
with open("config.json", "r") as read_file:
    config = json.load(read_file)

while (not connected):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=config['DOCKER-HOST']))
        channel = connection.channel()

        channel.queue_declare(queue='hello')
        connected = True

    except pika.exceptions.ConnectionClosedByBroker:
            print("Connection interrupted, retrying...")
            time.sleep(1)
            continue

    except pika.exceptions.AMQPConnectionError:
            print("Connection not available, retrying...")
            time.sleep(1)
            continue

def publish_message(message):
    channel.basic_publish(exchange='', routing_key='hello', body=message)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        greetings = greetings_pb2.Greetings()
        if request.form.get('action1') == 'Good morning':
            greetings.greetings = "Good morning"
            publish_message(greetings.SerializeToString())
        elif  request.form.get('action2') == 'Good evening':
            greetings.greetings = "Good evening"
            publish_message(greetings.SerializeToString())
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

