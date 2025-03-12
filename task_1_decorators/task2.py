import logging
import os
from contextlib import suppress
logging.basicConfig(level=logging.INFO, filename="py_log2.log",filemode="w")

def suppressException(exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with suppress(exception):
                result = func(*args, **kwargs)
                logging.info("Function executed successfully")
                return result
            logging.info(f"Exception occurred: {exception}")
            return None
        return  wrapper
    return decorator

@suppressException(FileNotFoundError)
def remove_file(filename):
    os.remove(filename)

remove_file("a_file.txt") # file does not exist