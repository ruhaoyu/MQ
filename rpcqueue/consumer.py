"""
@file: consumer.py
@author: rrh
@time: 2020/2/4 11:29 上午
"""


import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = conn.channel()

# channel.queue_declare(queue='producter_queue')


def call_back(channel, method, properties, body):
    print(properties)
    print(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    pass


channel.basic_consume(queue='producter_queue', consumer_callback=call_back, no_ack=False)
channel.start_consuming()
