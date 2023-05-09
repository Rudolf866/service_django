import json
import pika
from configuration.logger import info_log as logger


def get_connection_channel():
    logger.info(f"<<< start function get_connection_channel")

    credentials = pika.PlainCredentials('admin', 'qaz1986qaz')
    connection = pika.BlockingConnection(pika.ConnectionParameters('77.222.42.181', 5672, '/', credentials))
    channel = connection.channel()
    logger.info(f"Channel created")
    return channel, connection


def close_connection_channel(channel, connection):
    logger.info(f"<<< start function close_connection_channel")
    channel.close()
    connection.close()
    logger.info(f"Channel закрыт")


def publish(method, body):
    logger.info(f"<<< start function publish")
    logger.debug(f"method {method}, body {body}")
    channel, connection = get_connection_channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='direct', routing_key='severity', body=json.dumps(body), properties=properties)
    logger.info(f"==Отправлено==")
    close_connection_channel(channel, connection)
    # connection.close()
