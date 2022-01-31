import pika

def on_message_received(ch,method,properties,body):
    print(f"Analytics service - Received new message: {body.decode('utf-8')}")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()

# declaring our exchange
channel.exchange_declare(exchange="routing", exchange_type="direct")

# declaring queue
queue= channel.queue_declare(queue="", exclusive=True)

# binding queue
channel.queue_bind(exchange="routing", queue= queue.method.queue, routing_key="analyticsonly")

channel.basic_consume(queue = queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("[x] Analytics Consumer waiting for message")

channel.start_consuming()