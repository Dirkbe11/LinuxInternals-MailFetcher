import configparser
from MailFetcher.MailService import MailService

import logging
logger = logging.getLogger(__name__)

def main():
	
	logger.debug('Parsing config.ini...')
	config = configparser.ConfigParser()
	config.read('config.ini')
	mail_server = config['MailSettings']['MailServer']
	mail_address = config['MailSettings']['MailAddress']
	mail_password = config['MailSettings']['MailPassword']

	logger.debug('Booting up MailService...')
	service = MailService(mail_server, mail_address, mail_password)
	service.run()

	logger.debug('Exiting MailFetcher!')

if __name__ == "__main__":
	main()