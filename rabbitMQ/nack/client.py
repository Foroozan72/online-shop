import pika


credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()


ch.exchange_declare('aj',exchange_type='fanout')

while True :
    ch.basic_publish(exchange='aj',routing_key='home' ,body='sent message ...')
    print('sent ...!')
    input('pressany key to continue')