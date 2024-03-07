import pika

credentials = pika.PlainCredentials("foroozan" , "123")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost' , credentials = credentials))
ch = connection.channel()



ch.queue_declare('queue-request')

def on_request_message_recived(ch , method , properties , body ):
    print(f'Recived Request: {properties.correlation_id}')
    ch.basic_publish('' ,routing_key=properties.reply_to , body=f'Reply to {properties.correlation_id}' )


ch.basic_consume('queue-request' , on_message_callback=on_request_message_recived)
    

print('Start concuming . . ..')

ch.start_consuming()
