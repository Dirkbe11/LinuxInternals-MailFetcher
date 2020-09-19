import imaplib

import logging
logger = logging.getLogger(__name__)

class MailService():
	def __init__(self, server, address, password):
		logger.debug('Initializing Mail Service...')
		self.server = server
		self.address = address
		self.password = password


		print(address)
		print(password)

		self.connection = imaplib.IMAP4_SSL(server)
		self.connection.login(address, password)
		self.connection.select('INBOX')





	def run(self):
		logger.debug('Running Mail Service')
		# while(True):
		status, response = self.connection.search(None, '(UNSEEN)')
		unread_msg_nums = response[0].split()

		msg = unread_msg_nums[0]
		status, data = self.connection.fetch(msg, '(RFC822)')
		email_msg = data[0][1]



		print("unread mail count: {}".format(len(unread_msg_nums)))


		print("FIRST MESSAGE: \n\n{}".format(email_msg))

