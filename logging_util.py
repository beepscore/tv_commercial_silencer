# https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
import logging
import sys


def get_logger(name):
    """
    Log to stream only. Don't add a handler to log to a file.
    Let program user decide if they want to pipe stream output to a file e.g.
        python3 fibonacci.py >> ../fib.log
        python3 -m unittest >> ../test.log

    References
    https://12factor.net/logs
    "logging in an application"
    https://docs.python-guide.org/writing/logging/

    https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
    https://stackoverflow.com/questions/28330317/print-timestamp-for-logging-in-python
    https://docs.python.org/3/library/logging.html#formatter-objects
    https://docs.python.org/3.6/howto/logging.html#logging-basic-tutorial
    https://docs.python.org/3.6/howto/logging.html#logging-to-a-file

    :param name: logger name
    :return: a configured logger
    """
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(funcName)s line:%(lineno)s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # add one or more handlers

    # log stream to terminal stdout. program user can choose to pipe stream to a file.
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

    # Don't log to file. See docstring for rationale.
    # mode 'a' append, not 'w' write
    # handler = logging.FileHandler('./data/output/fib.log', mode='a')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    return logger

