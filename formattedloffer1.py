import logging


logging.basicConfig(filename='kkar_logs.log', filemode='w',
format='%(levelname)s = %(asctime)s: %(message)s',
                    level=logging.ERROR)

logging.debug("Debugging")
logging.info("Information")
logging.warning("Warning")
logging.error("error")
logging.fatal("fatal")
