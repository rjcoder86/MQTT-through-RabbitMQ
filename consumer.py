import pika
import json
from pymongo import MongoClient

# RabbitMQ connection parameters
rabbitmq_url = 'amqp://guest:guest@localhost/'
queue_name = 'test_queue'

# Connect to RabbitMQ server
parameters = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

mongo_uri = 'mongodb://localhost:27017/'
db_name = 'randomMessages'
collection_name = 'messages'

mongo_client = MongoClient(mongo_uri)
db = mongo_client[db_name]
collection = db[collection_name]

# Declare the queue
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    # Print the message body
    try:
        msg_body = json.loads(body.decode('utf-8'))
        collection.insert_one(msg_body)
        print("Received message:", msg_body)
    except json.JSONDecodeError:
        print("Failed to decode message:", body.decode('utf-8'))

# Set up a consumer to listen to the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Consumer stopped.')

# Close the connection
print('closing....')
connection.close()
