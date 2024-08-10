import pika
import random
import json
import time
from datetime import datetime

rabbitmq_host = 'localhost'
rabbitmq_queue = 'msg_queue'


connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queue)

def generate_random_message():
    message = {
        'status': random.randint(0,6),
        'timestring': datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
    }
    return json.dumps(message)

try:
    while True:
        message = generate_random_message()
        channel.basic_publish(exchange='',routing_key=rabbitmq_queue,body=message)
        print(f"message: {message}")
        time.sleep(1)
except Exception as e:
    print(str(e))

connection.close()
