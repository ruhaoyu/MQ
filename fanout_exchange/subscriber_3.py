"""
@file: subscriber_1.py
@author: rrh
@time: 2020/1/15 12:53 下午
"""
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = conn.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)

channel.queue_declare(queue='queue_3', durable=True)
channel.queue_bind(queue='queue_3', exchange='logs', routing_key='bind_queue_3')


def call_back(channel, method, properties, body):
    print(properties)
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(consumer_callback=call_back, queue='queue_3', no_ack=False)

channel.start_consuming()

