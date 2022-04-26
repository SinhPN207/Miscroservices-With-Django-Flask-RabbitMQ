import pika

params = pika.URLParameters('amqps://zjkkqgxy:Em9iKJW3YkmGlv7xmoeJJ4iyh-s5HbpA@armadillo.rmq.cloudamqp.com/zjkkqgxy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
