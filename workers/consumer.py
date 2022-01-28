import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

#declare again here
channel.queue_declare(queue="task_queue", durable=True) # if message is not consumed and rabbitmq server goes down then durable=True will save our message

def callback(ch,method,properties,body):
    print("[x] Received %r" % body.decode())
    time.sleep(body.count(b".")) #receiver is 
    
    ch.basic_ack(delivery_tag=method.delivery_tag)

#this consumer will fetch only one message at a time
# if this worker is busy with one task then this worker wont get another message
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="task_queue", on_message_callback=callback) #not giving auto_ack=True here as done in hello-world example. We will do it in callback function

print("[*] Waiting for messages to exit press ctrl + c")
channel.start_consuming()