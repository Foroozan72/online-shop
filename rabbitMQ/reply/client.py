import pika
import uuid

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()

reply_queue = ch.queue_declare(queue='',exclusive=True)

def on_reply_recive(ch , method , propertiese , body):
    print(f'Recived {body}')

ch.basic_consume(queue=reply_queue.method.queue , on_message_callback= on_reply_recive , auto_ack=True)

ch.queue_declare('queue-request')
cor_id = str(uuid.uuid4())
ch.basic_publish(exchange='' ,routing_key='queue-request' , properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue ,
    correlation_id = cor_id ,),
    body = 'Can i request a reply? '
                                                                                            ) 

print(f'Sending Request {cor_id}')

ch.start_consuming()



