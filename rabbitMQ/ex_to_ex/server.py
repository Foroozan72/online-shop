import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()

ch.exchange_declare(exchange='to' , exchange_type='fanout')
ch.queue_declare(queue='frzn')
ch.queue_bind('frzn' ,'to')


def calling(ch , method , properties , body ):
    print(f'the message Received {body}')

ch.basic_consume(queue='frzn' , on_message_callback=calling , auto_ack=True)

print('start consuming ...')

ch.start_consuming()
