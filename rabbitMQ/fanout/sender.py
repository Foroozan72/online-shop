import pika

credencials =pika.PlainCredentials('foroozan' , '123') 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials=credencials))
ch = connection.channel()

ch.exchange_declare(exchange='logs' , exchange_type='fanout')

ch.basic_publish(exchange='logs' , routing_key='' ,body='FANOUT...!')

print('massage sent')
connection.close()