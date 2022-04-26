import pika, json

from app import Product, db

params = pika.URLParameters('amqps://zjkkqgxy:Em9iKJW3YkmGlv7xmoeJJ4iyh-s5HbpA@armadillo.rmq.cloudamqp.com/zjkkqgxy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.comit()

    elif properties.content_type == 'product_update':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.comit()

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.comit()


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
