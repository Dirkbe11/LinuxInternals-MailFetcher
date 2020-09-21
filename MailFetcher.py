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

	mail_producer_topic = config['KafkaSettings']['ProducerTopic']
	kafka_settings = config['KafkaSettings']['ServerSettings']

	logger.debug('Booting up MailService...')
	service = MailService(mail_server, mail_address, mail_password, mail_producer_topic, kafka_settings)
	service.run()

	logger.debug('Exiting MailFetcher!')

if __name__ == "__main__":
	main()