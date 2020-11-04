import logging

logging.basicConfig(filename='kkar_logs.log',
    filemode='w',format='%(levelname)s: %(message)s',
                    level=logging.WARN)

logging.debug("Debugging.")
logging.info("Information")
logging.warning("Warning")
logging.error("Errors")
logging.critical("High Priority Message")