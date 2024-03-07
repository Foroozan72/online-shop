import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()


ch.exchange_declare(exchange='main' , exchange_type='direct')
ch.exchange_declare(exchange='edtl' , exchange_type='fanout')

ch.queue_declare(queue='mainq' ,arguments={'x-dead-letter-exchange':'edtl' , 'x-message-ttl':5000 , 'x-max-length':100 ,})
ch.queue_bind(queue='mainq',exchange='main',routing_key='home')

ch.queue_declare('edtlq')
ch.queue_bind('edtlq','edtl')

def edtl_callback(ch,method,properties,body):
    print(f'the deadletter {body}')

ch.basic_consume(queue='edtlq',on_message_callback=edtl_callback , auto_ack=True)

print('start consuming ...')

ch.start_consuming()

