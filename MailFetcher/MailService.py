from imapclient import IMAPClient
import email

from .MailProducer import MailProducer

import logging
logger = logging.getLogger(__name__)

class MailService():
	def __init__(self, server, address, password, producer_topic, kafka_settings):
		logger.debug('Initializing Mail Service...')
		self.server = server
		self.address = address
		self.password = password
		self.mail_producer = MailProducer(producer_topic, kafka_settings)


	def run(self):
		logger.debug('Running Mail Service')

		with IMAPClient(self.server) as server:
			server.login(self.address, self.password)
			server.select_folder('INBOX')

			messages = server.search('UNSEEN')
			
			logger.debug("Processing {} messages")
			print("Message count: {}".format(len(messages)))

			for uid, message_data in server.fetch(messages, 'RFC822').items():
				email_message = email.message_from_bytes(message_data[b'RFC822'])
				self.mail_producer.send_mail(uid, email_message)
