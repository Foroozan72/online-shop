import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt' , exchange_type='fanout')
ch.exchange_declare(exchange='main' , exchange_type='direct' , arguments={'alternate-exchange':'alt'})


ch.queue_declare(queue='altq')
ch.queue_bind('altq','alt')

ch.queue_declare(queue='mainq')
ch.queue_bind('mainq','main' , 'home')

def call_main(ch , method ,properties , body):
    print(f'Received main {body}')

def call_alt(ch , method ,properties ,body):
    print(f'Received alternative {body}')

ch.basic_consume(queue='altq',on_message_callback=call_alt , auto_ack=True)
ch.basic_consume(queue='mainq',on_message_callback=call_main , auto_ack=True)


print('start consuming ...')

ch.start_consuming()