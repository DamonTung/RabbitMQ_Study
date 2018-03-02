import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='dt')
print("[x] Waiting for message. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))


channel.basic_consume(callback, queue='dt', no_ack=True)
channel.start_consuming()