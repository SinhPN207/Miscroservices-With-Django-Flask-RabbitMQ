import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://zjkkqgxy:Em9iKJW3YkmGlv7xmoeJJ4iyh-s5HbpA@armadillo.rmq.cloudamqp.com/zjkkqgxy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    print(product)
    product.likes = product.likes + 1
    product.save()


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
