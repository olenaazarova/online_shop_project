import json
import pika
import os

from dotenv import load_dotenv

load_dotenv()


class EventProducer:

    @staticmethod
    def publish_event(event_type: str, payload: dict):

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_HOST")
            )
        )

        channel = connection.channel()

        channel.queue_declare(queue="items-events")

        message = {
            "event": event_type,
            "data": payload
        }

        channel.basic_publish(
            exchange='',
            routing_key='items-events',
            body=json.dumps(message)
        )

        connection.close()