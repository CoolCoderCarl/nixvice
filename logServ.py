import os
import logging

log_path = '/var/log/'

# init log settings
def log_init():
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # set basic logger config
    logging.basicConfig(filename=str(log_path) + 'test-python-service.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info('PID:' + str(os.getpid()))

    print('Log initiated')

def make_logs():
    logging.info('OS name ' + os.name)
    logging.info('Current work dir ' + os.getcwd())
