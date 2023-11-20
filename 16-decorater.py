import time

def logger(fn):
    def wrapper():
        print(time.time())
        fn()
        print(time.time())


    return wrapper

@logger
def do_some_more():
    print("Print some more")


@logger
def do_something():  
    print("Print something")
    

do_something()