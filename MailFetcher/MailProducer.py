from kafka import KafkaProducer

from .ProtoBuff import EmailMessage_pb2

import logging
logger = logging.getLogger(__name__)

class MailProducer:
	def __init__(self, producer_topic, kafka_settings):
		logger.debug('Initializing Mail Producer...')

		self.producer_topic = producer_topic
		self.kafka_settings = kafka_settings
		self.kafka_producer = KafkaProducer(bootstrap_servers=kafka_settings)

	def send_mail(self, uid, email_message):

		email_message_proto = EmailMessage_pb2.EmailMessage()
		email_message_proto.uid = uid
		email_message_proto.sent_to = email_message.get('To')
		email_message_proto.sent_from = email_message.get('From') 
		email_message_proto.message_id = email_message.get('message-id')

		if email_message.is_multipart():
			for part in email_message.walk():
				if part.get_content_type() == 'text/plain':
					email_message_proto.message_body = part.get_payload();
		else:
			email_message_proto.message_body = email_message.get_payload()

		if email_message.get('in_reply_to') != None:
			email_message_proto.in_reply_to = email_message.get('in_reply_to')


		logger.debug("Emitting message to broker: {}".format(uid))
		self.kafka_producer.send(self.producer_topic, email_message_proto.SerializeToString())


		