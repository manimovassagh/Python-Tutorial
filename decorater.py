import time

def logger(function):
    def wrapper():
        print(time.localtime())
        function()
        print(time.localtime())

    return wrapper


@logger
def check():
    print("This is a check function")
    print(time.time())


check()

