import pika
import time

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()

ch.queue_declare(queue='one')
ch.basic_publish(exchange='' , routing_key='one' , body='helow ....' , properties=pika.BasicProperties(
    # content_type='text/plain',
    # content_encoding='gzip',
    headers={"name":"foroozan" , "age":"30"} 
    # ,
    # expiration=str(time.time()) ,
    # timestamp=100000000000 ,
    # type="exch.queue",
    # user_id="10" ,
    # app_id="500" ,
    # delivery_mode=2
    )
)
print('message sent ... !')
connection.close()