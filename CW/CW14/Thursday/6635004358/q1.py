import logging

def fib_log(msg):

    logger = logging.getLogger(__name__)

    file_handler1 = logging.FileHandler("fib.log")

    formater = logging.Formatter('%(levelname)s %(asctime)s %(name)s %(lineno)d %(message)s')

    file_handler1.setFormatter(formater)
    file_handler1.setLevel(logging.ERROR)

    logger.addHandler(file_handler1)

    return logger.exception(msg)
# logger_fib = logging.getLogger(__name__)
#
# file_handler_fib = logging.FileHandler("fib.log")
#
# formater = logging.Formatter('%(levelname)s %(asctime)s %(name)s %(lineno)d %(message)s')
#
# file_handler_fib.setFormatter(formater)
# file_handler_fib.setLevel(logging.ERROR)
#
# logger_fib.addHandler(file_handler_fib)
#
# logger_isprime = logging.getLogger(__name__)
#
# file_handler_prime = logging.FileHandler("isprime.log")
#
# file_handler_prime.setFormatter(formater)
# file_handler_prime.setLevel(logging.ERROR)
#
# logger_isprime.addHandler(file_handler_prime)
#
# print(logger_fib is logger_isprime)

# try:
#     number = int(input(">>"))
#     print(myMath.fibo(number))
# except ValueError:
#     logger_fib.error("incorrect input")
#
#
# try:
#     number = int(input(">>"))
#     print(myMath.isprime(number))
# except ValueError:
#     logger_isprime.error("number must be an integer")
