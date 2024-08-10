import pika
import random
import json
import time
from datetime import datetime

# RabbitMQ connection parameters
rabbitmq_host = 'localhost'
rabbitmq_queue = 'test_queue'

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=rabbitmq_queue)

def generate_random_message():
    """Generate a random message."""
    message = {
        'status': random.randint(0,6),
        'timestamp': datetime.fromtimestamp(time.time()).strftime('%H:%M:%S'),
        # 'timestamp': datetime.fromtimestamp(time.time()).time()
    }
    return json.dumps(message)

try:
    while True:
        # Generate a random message
        message = generate_random_message()
        # Publish the message to RabbitMQ
        channel.basic_publish(exchange='',
                              routing_key=rabbitmq_queue,
                              body=message)
        print(f"Published message: {message}")
        # Wait for a bit before publishing the next message
        time.sleep(5)  # Adjust sleep time as needed
finally:
    # Close the connection
    connection.close()
