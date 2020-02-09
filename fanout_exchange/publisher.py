"""
@file: publisher.py
@author: rrh
@time: 2020/1/15 12:47 下午
"""
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = conn.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout', durable=True)
channel.queue_declare(queue='queue_1', durable=True)
channel.queue_declare(queue='queue_2', durable=True)
channel.queue_declare(queue='queue_3', durable=True)

channel.basic_publish(exchange='logs',
                      body='hello you and hello me',
                      routing_key='',
                      properties=pika.BasicProperties(delivery_mode=2))

channel.close()

