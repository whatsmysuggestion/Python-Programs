import logging


logging.basicConfig(filename='kkar_logs.log', filemode='w',
                    format='%(levelname)s -> %(asctime)s:'
                           ' %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("custom logging.")
shubham = {'name': 'Shubham', 'roll': 1}
logger.debug("Shubham: %s" ,shubham)