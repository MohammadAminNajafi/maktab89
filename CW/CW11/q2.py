import logging

def prime_log():
    logger = logging.getLogger(__name__)

    file_handler1 = logging.FileHandler("isprime.log")

    formater = logging.Formatter('%(levelname)s %(asctime)s %(name)s %(lineno)d %(message)s')

    file_handler1.setFormatter(formater)
    file_handler1.setLevel(logging.ERROR)

    logger.addHandler(file_handler1)

    return logger.error("incorrect input for prime")