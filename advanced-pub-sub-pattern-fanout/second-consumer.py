import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

def on_message_received(ch,method,properties,body):
    print(f"secondconsumer: received new message : {body.decode()}")

channel.exchange_declare(exchange="pubsub", exchange_type="fanout")

# exclusive tells that once the consumer is closed queue can be deleted
queue = channel.queue_declare(queue="",exclusive=True) # server will choose random queue name
queue_name = queue.method.queue
print(f"queue name : {queue_name}")
channel.queue_bind(exchange="pubsub",queue=queue_name)

channel.basic_consume(queue = queue_name, auto_ack=True, on_message_callback=on_message_received)

print("[x] Second Consumer waiting for message")

channel.start_consuming()