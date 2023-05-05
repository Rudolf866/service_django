import json
import pika


def get_connection_channel():
    print("Creating MQ connection channel on local host")
    credentials = pika.PlainCredentials('root', 'root')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
    channel = connection.channel()
    print("Channel created")
    return channel, connection


def close_connection_channel(channel, connection):
    channel.close()
    connection.close()
    print("Channel закрыт")


def publish(method, body):
    channel, connection = get_connection_channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='direct', routing_key='severity', body=json.dumps(body), properties=properties)
    print("==Отправлено==")
    close_connection_channel(channel, connection)
    # connection.close()
