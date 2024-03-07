import pika

credencials =pika.PlainCredentials('foroozan' , '123') 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credencials))
ch = connection.channel()

ch.exchange_declare(exchange='topic_log' , exchange_type='topic')

massages = {
    'error.warnning.important' : 'the errro is important' ,
    'debug.info.notimportant' : 'ignor the error'
}

for k , v in massages.items():
    ch.basic_publish(exchange='topic_log' , routing_key=k , body=v)

print('message sent')
connection.close()