import pika
import json
from mongo_connector import MongoConnector
from datetime import datetime

rabbitmq_url = 'amqp://guest:guest@localhost/'
queue_name = 'msg_queue'

parameters = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue=queue_name)

connector = MongoConnector()
connector.connect()

def callback(ch, method, properties, body):
    try:
        msg_body = json.loads(body.decode('utf-8'))
        time_obj = datetime.strptime(msg_body['timestring'], '%H:%M:%S').time()
        msg_body['timestamp'] =  datetime.combine(datetime.today(), time_obj)
        connector.insert_data(msg_body)
        print("Received message:", msg_body)
    except Exception as e:
        print("Error", str(e))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print('Consumer stopped.')


connection.close()
