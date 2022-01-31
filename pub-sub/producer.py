import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
channel.exchange_declare(exchange="logs", exchange_type="fanout")


message = ' '.join(sys.argv[1:]) or "pub-sub message"

channel.basic_publish(exchange="logs",#one receiver should receive the message
 routing_key="",
body=message
)

print("[x] Sent %r"%message)

channel.close()

