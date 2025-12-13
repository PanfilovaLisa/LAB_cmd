import logging

def make_log():
    logging.basicConfig(level=logging.INFO, filename='shell.log', format='%(asctime)s %(message)s')
    return

def log_in(line):
    """
    Делает запись в файле shell.log

    Аргументы:
        line - текст для записи
    """
    logging.info(line)
    return


def get_mistake(func):
    """
    Декоратор для функций.

    Аргументы:
        func - декорируемая функция

    Декоратор принимает сообщение об ошибке во время исполнения - RESULT. Выводит сообщение в терминал и делает
    соответствующую запись в shell.log. Возвращает False для завершения декорируемой функции.
    """
    def wrapper(*args):
        RESULT = func(*args)
        if type(RESULT) == str:
            print(RESULT)
            log_in('ERROR: ' + RESULT)
            return False 
        return True
    return wrapper