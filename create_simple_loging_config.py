import logging
import logging.config
#Logging to a File
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s', filename='sample.txt', encoding='utf-8')
logging.info('Hello World')
