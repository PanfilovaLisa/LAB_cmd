import logging

def make_log():
    logging.basicConfig(level=logging.INFO, filename='shell.log', format='%(asctime)s %(message)s')
    return

def log_in(line):
    logging.info(line)
    return


def get_mistake(func):
    def wrapper(*args):
        RESULT = func(*args)
        if RESULT!=True:
            print(RESULT)
            log_in('ERROR: ' + RESULT)
            return False 
        return True
    return wrapper