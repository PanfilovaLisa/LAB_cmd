import logging

def make_log():
    logging.basicConfig(level=logging.INFO, filename='shell.log', format='%(asctime)s %(message)s')
    return

def log_in(line):
    logging.info(line)
    return