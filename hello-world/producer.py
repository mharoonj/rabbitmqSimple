import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="hello world")

channel.close()


# from pyrabbit.api import Client
# cl = Client('localhost:15672', 'guest', 'guest')
# queues = [q['name'] for q in cl.get_queues()]

import requests

# def rest_queue_list(user='guest', password='guest', host='localhost', port=15672, virtual_host=None):
#     url = 'http://%s:%s/api/queues/%s' % (host, port, virtual_host or '')
#     response = requests.get(url, auth=(user, password))
#     # print(response.json())
#     queues = [q['name'] for q in response.json()]
#     return queues

# print(rest_queue_list())