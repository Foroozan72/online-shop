import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()

ch.exchange_declare(exchange='alt' , exchange_type='fanout')
ch.exchange_declare(exchange='main' , exchange_type='direct' , arguments={'alternate-exchange':'alt'})

ch.basic_publish(exchange='main' , routing_key='home' , body='if sth wronge goes on , switch on alternative exchange')


print('message sent ...')

connection.close()