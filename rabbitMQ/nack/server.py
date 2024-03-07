import pika


credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()


ch.exchange_declare('aj',exchange_type='fanout')
ch.queue_declare('main')
ch.queue_bind(queue='main' , exchange='aj')



def callback(ch , method , properties , body):
    if method.delivery_tag % 5 == 0 :
        ch.basic_nack(delivery_tag=method.delivery_tag , request=False , multiply =True)
        print(f'Recived {method.delivery_tag} ')


ch.basic_consume(queue='main' , on_message_callback=callback)
print('Stat Consuming ...')
ch.start_consuming()
