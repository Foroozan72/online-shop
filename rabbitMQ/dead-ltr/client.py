import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()


ch.exchange_declare(exchange='main' , exchange_type='direct')
ch.basic_publish(exchange='main' , routing_key='home' , body='there is no problem')

print('sent ...')
connection.close()