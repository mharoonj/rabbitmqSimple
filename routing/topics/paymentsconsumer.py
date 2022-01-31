import pika

def on_message_received(ch,method,properties,body):
    print(f"Payment service - Received new message: {body.decode('utf-8')}")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

# declaring our exchange
channel.exchange_declare(exchange="mytopicexchange", exchange_type="topic")

# declaring queue
queue= channel.queue_declare(queue="", exclusive=True)

# binding queue
channel.queue_bind(exchange="mytopicexchange", queue= queue.method.queue, routing_key="#.payments") # any routing key like order.payments or anything with .payments will work


channel.basic_consume(queue = queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("[x] Payment Consumer waiting for message")

channel.start_consuming()

