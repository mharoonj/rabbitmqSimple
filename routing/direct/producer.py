import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type="direct")

message = "hello, this message needs to be routed"
routing_key = "analyticsonly"  # or paymentsonly or both
channel.basic_publish(exchange="routing", routing_key=routing_key, body=message)

print(f'sent message : {message}, on route {routing_key}')

connection.close()

# to send message to both queues 
# channel.queue_bind(exchange="routing", routing_key=routing_key, body=message)
