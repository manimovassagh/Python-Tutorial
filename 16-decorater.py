from datetime import datetime

def logger(function):
    def wrapper():
        print(datetime.now())
        function()
        print(datetime.now())
    return wrapper


@logger
def check():
    print("This is a check function")

check()