from contextlib import ContextDecorator
import logging
import time

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")


class track_entry_and_exit(ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        logging.info('Entering: %s', self.name)

    def __exit__(self, exc_type, exc, exc_tb):
        elapsed_time = time.time() - self.start_time
        logging.info('Exiting: %s | Execution time: %.4f seconds', self.name, elapsed_time)


@track_entry_and_exit('sleep')
def activity():
    time.sleep(5)


activity()
