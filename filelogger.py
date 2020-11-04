import logging


logging.basicConfig(filename = 'kkar_logs.log',
                    filemode='w',level = logging.WARN)
logging.debug("Debugging")
logging.info("Information")
logging.warning("Warning")
logging.error("Error Message")
logging.critical("High Priority")

#debug
#info
#warn
#error
#critical