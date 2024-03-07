import pika

credencials =pika.PlainCredentials('foroozan' , '123') 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credencials))
ch = connection.channel()


ch.exchange_declare(exchange='topic_log' , exchange_type='topic')

result = ch.queue_declare(queue='' , exclusive=True)

ch.queue_bind(queue=result.method.queue , exchange='topic_log' , routing_key='#.important')

print('Waiting for messages ...! ')

def callback(ch , method , properties , body):
    with open('error_log.log' , 'a') as el:
        el.write(f'{str(body)} \n')
        

ch.basic_consume(queue=result.method.queue ,on_message_callback= callback, auto_ack=True)

ch.start_consuming()