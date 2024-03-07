import pika 
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) 

ch = connection.channel()

ch.queue_declare(queue='one')

def callback(ch , method , properties , body):
    print(f'the massage {body} receive')
    print(properties.headers)
    print(method)
    time.sleep(5)
    print('Done! ')
    ch.basic_ack(delivery_tag = method.delivery_tag)



ch.basic_qos(prefetch_count=1) 

ch.basic_consume(queue='one' , on_message_callback=callback )  
# , auto_ack=True

print ('Waiting for message, prees ctrl+c to exit')

ch.start_consuming()



