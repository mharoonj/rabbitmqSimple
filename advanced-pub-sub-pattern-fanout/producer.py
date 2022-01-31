import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="pubsub", exchange_type="fanout")

message = "hello i want to brodcast this message"

channel.basic_publish(exchange="pubsub", routing_key="", body=message)

print(f'sent message : {message}')

connection.close()