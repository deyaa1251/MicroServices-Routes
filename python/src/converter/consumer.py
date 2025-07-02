import pika, sys, os, time
from pymongo import MongoClient
import gridfs
from convert import to_mp3

def main():
	client = MongoClient("host.minikube.internal", 27017 )
	db_videos = client.videos
	db_mp3s = client.mp3s
	#gridfs
	fs_videos = gridfs.GridFS(db_videos)
	fs_mp3s = gridfs.GridFS(db_mp3)

	# Rabbitmq connection
	connection = pika.BlockingConnection(
		pika.ConnectionParameters(host="rabbitmq")
	)

	channel = connection.channel()
	def callback(ch, method, properties, body):
		err = to_mp3.start(body, fs_video, fs_mp3s, ch)
		if err:
			ch.basic_nack(delivery_tag=method.delivery_tag)
		else:
			ch.basic_ack(delivery_tag=method.delivey_tag)
	channel.basic_consume(
		queue=os.environ.get("VIDEO_QUEUE"), on message_callback=callback
	)

	print("Waiting for messages")
	
	channel.start_consuming()
	
if __name__ = "__main_":
	try:
		main()
	except KeyboardInterrupt:
		print("Interrupted ")
		try:
			sys.exit(0)
		except SystemExit:
			os.exit(0)
