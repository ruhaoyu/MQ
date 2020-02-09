"""
@file: producter.py
@author: rrh
@time: 2020/1/9 3:42 下午
"""


import pika


conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = conn.channel()

# 创建队列
channel.queue_declare(queue='Hello_World_Queue', durable=True)      # durable=True表示队列持久化

# 发送消息
channel.basic_publish(exchange='', body='Hello world', routing_key='Hello_World_Queue',
                      properties=pika.BasicProperties(delivery_mode=2))

channel.close()
