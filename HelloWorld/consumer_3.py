"""
@file: consumer_1.py
@author: rrh
@time: 2020/1/9 3:42 下午
"""

import pika


conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = conn.channel()

channel.queue_declare(queue='Hello_World_Queue')


def call_back(channel, method, properties, body):
    print(properties)
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='Hello_World_Queue', consumer_callback=call_back, no_ack=False)

channel.start_consuming()
