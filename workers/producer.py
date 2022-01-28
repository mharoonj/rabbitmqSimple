import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()
message = ' '.join(sys.argv[1:]) or "Task_queue message"
channel.queue_declare(queue="task_queue", durable=True) # if message is not consumed and rabbitmq server goes down then durable=True will save our message

channel.basic_publish(exchange="",#one receiver should receive the message
 routing_key="task_queue",
body=message,
properties=pika.BasicProperties(delivery_mode = 2) # this will go hand in hand with durable = True mentioned above
)

print("[x] Sent %r"%message)

channel.close()

