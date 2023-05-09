import json
import os
import django
import pika
from configuration.logger import info_log as logger

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from app.models import Post


def main():
    logger.info(f"<<< start function main()")
    credentials = pika.PlainCredentials('admin', 'qaz1986qaz')
    connection = pika.BlockingConnection(pika.ConnectionParameters('77.222.42.181', 5672, '/', credentials))
    channel = connection.channel()

    result = channel.queue_declare(queue='post', durable=True)
    channel.exchange_declare(exchange='direct', exchange_type='direct')
    queue_name = result.method.queue
    channel.queue_bind(
        exchange='direct', queue=queue_name, routing_key='severity')

    def callback(ch, method, properties, body):
        logger.debug(" [x] %r:%r" % (method.routing_key, body.decode()))
        output_dict = json.loads(body.decode("utf-8"))
        logger.debug(f"output_dict {output_dict['method'] }")
        logger.debug(f"properties {properties.content_type}")

        posts = Post.objects.all()
        if properties.content_type == 'create-post':
            quote = Post.objects.create(title=output_dict["title"], text=output_dict["text"])
            quote.save()
            print("post-created")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
