import queue
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

#declare again here
channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue='', exclusive=True) #generating queue by itself
queue_name = result.method.queue #getting queue name by variable result

#consumer will bind to queue only 
#so for binding it 
channel.queue_bind(exchange="logs", queue=queue_name)

def callback(ch,method,properties,body):
    print("[x] Received %r" % body.decode())
    

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("[*] Waiting for messages to exit press ctrl + c")
channel.start_consuming()