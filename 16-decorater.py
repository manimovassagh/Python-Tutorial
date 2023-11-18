from datetime import datetime
import time
def logger(function):
    def wrapper():
        print(datetime.now())
        function()
        print(datetime.now())
    return wrapper


@logger
def check():
    print("This is a check function")
    print(time.now())    


check()




