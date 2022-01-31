import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="mytopicexchange", exchange_type="topic")

message = "hello, this message needs to be routed"
routing_key = "user.europe.payments"  
channel.basic_publish(exchange="mytopicexchange", routing_key=routing_key, body=message)
channel.basic_publish(exchange="mytopicexchange", routing_key="business.europe.order", body="business message")

print(f'sent message : {message}, on route {routing_key}')

connection.close()

# to send message to both queues 
# channel.queue_bind(exchange="routing", routing_key=routing_key, body=message)
