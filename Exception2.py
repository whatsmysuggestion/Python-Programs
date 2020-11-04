import logging
try:
    logging.info("Entered Try Block")
    open("ddd.txt","r")
    a=10
    b='e'
    c=a/b
    print(c)
    logging.info("Exited Try Block")
except FileNotFoundError:
    logging.critical("FileNotFoundError Occured")
    print("Error Occured")
except TypeError:
    logging.critical("TypeError Occured")
    print("Error Occured Please try again")
except Exception:
    logging.critical("Some Other Error Occured")
    print("Some Other Error Occured Please try again")







