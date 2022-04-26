import json

import pika

params = pika.URLParameters('amqps://zjkkqgxy:Em9iKJW3YkmGlv7xmoeJJ4iyh-s5HbpA@armadillo.rmq.cloudamqp.com/zjkkqgxy')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
