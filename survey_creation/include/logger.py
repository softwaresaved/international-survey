#!/usr/bin/env python
# encoding: utf-8

import os
import logging
from logging.handlers import RotatingFileHandler


def logger(name='logger', logger_level='DEBUG', file_level='INFO', stream_level='CRITICAL',
           size=10000, backup=10):

    logger = logging.getLogger(name)
    logger_set_level = getattr(logging, logger_level)
    logger.setLevel(logger_set_level)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')

    stream_handler = logging.StreamHandler()
    stream_set_level = getattr(logging, stream_level)
    stream_handler.setLevel(stream_set_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    if file_level is not None:
        try:
            os.mkdir('logs')
        except OSError:
            pass
        file_location = './logs/{}.log'.format(name)
        file_handler = RotatingFileHandler(filename=file_location,
                                           mode='a', maxBytes=size,
                                           backupCount=backup)
        file_set_level = getattr(logging, file_level)
        file_handler.setLevel(file_set_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def main():
    """ """
    pass

if __name__ == '__main__':
    main()
