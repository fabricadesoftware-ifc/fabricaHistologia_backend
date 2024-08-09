import pika

credentials = pika.PlainCredentials('lucas', '240600')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', virtual_host='fabricahistologia', credentials=credentials))
channel = connection.channel()

print("Conectado com sucesso ao RabbitMQ!")
