import json
import pika
import os
import time

from dotenv import load_dotenv

from app.db.database import search_collection

load_dotenv()


def process_message(message):

    event = message["event"]
    data = message["data"]

    if event == "ITEM_CREATED":

        search_collection.insert_one(data)

    elif event == "ITEM_UPDATED":

        search_collection.update_one(
            {
                "id": data["id"]
            },
            {
                "$set": data
            }
        )

    elif event == "ITEM_DELETED":

        search_collection.delete_one(
            {
                "id": data["id"]
            }
        )


def callback(ch, method, properties, body):

    message = json.loads(body)

    process_message(message)


def start_consumer():

    while True:

        try:

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=os.getenv("RABBITMQ_HOST")
                )
            )

            channel = connection.channel()

            channel.queue_declare(
                queue="items-events"
            )

            channel.basic_consume(
                queue="items-events",
                on_message_callback=callback,
                auto_ack=True
            )

            print("Waiting for events...")

            channel.start_consuming()

        except Exception as e:

            print("RabbitMQ connection failed:")
            print(e)

            time.sleep(5)