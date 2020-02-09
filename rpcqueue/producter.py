"""
@file: producter.py
@author: rrh
@time: 2020/2/4 11:28 上午
"""

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = conn.channel()

# channel.exchange_declare(exchange='Producter_exchange', durable=True)
channel.queue_declare(queue='producter_queue', durable=True)

# channel.queue_bind(queue='producter_queue', exchange='producter_queue')


channel.basic_publish(exchange='', body='111111', routing_key='producter_queue',
                      properties=pika.BasicProperties(delivery_mode=2))

channel.close()
