import logging
from utility import Utility
from db import db

class App:

    def __init__(self):  
        self._util = Utility()
        self._util.ConfigureLogging()

    def Process(self):
        try:
            logging.info('*** Start ***')
            mydb = db()
            mydb.Process()

            logging.info('*** Stop ***')
        except BaseException as ex:
            logging.exception(ex)

app = App()
app.Process()