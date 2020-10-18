import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, value):
        super(LoggableList, self).append(value)
        super(LoggableList, self).log(value)