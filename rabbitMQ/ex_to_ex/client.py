import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()


ch.exchange_declare(exchange='from' ,exchange_type='direct')
ch.exchange_declare(exchange='to' ,exchange_type='fanout')

ch.exchange_bind('to' , 'from')

ch.basic_publish(exchange='from' , routing_key='' , body='Done ... !')

print('message sent successfuly')

connection.close()