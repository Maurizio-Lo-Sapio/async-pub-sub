#!/usr/bin/env python
import pika, sys, os
import time
import json

from worker import Worker

def main():
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    host = config['DOCKER-HOST']
    worker = Worker()
    worker.start()

    while (True):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
            channel = connection.channel()

            channel.queue_declare(queue='hello')
            channel.basic_consume(queue='hello', on_message_callback=worker.callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()

        except pika.exceptions.ConnectionClosedByBroker:
            print(f'Connection interrupted with {host}, retrying...')
            time.sleep(1)
            continue

        except pika.exceptions.AMQPConnectionError:
            print(f'Connection not available with {host}, retrying...')
            time.sleep(1)
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
