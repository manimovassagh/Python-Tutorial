def logger(function):
    def wrapper():
        print("This is a logger decoraer")
        function()
    return wrapper


@logger
def check():
    print("This is a check function")

check()