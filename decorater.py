import time


def logger(fn):
    def wrapper():
        print(time.time())
        fn()
        print(time.time())

    return wrapper


@logger
def check():
    print("This is a check function")


check()
