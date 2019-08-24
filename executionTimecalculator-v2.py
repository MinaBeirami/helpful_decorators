
def time_this():
    print("decorating")

    def wrapper(function):
        from datetime import datetime
        ts=datetime.now()
        function()
        te=datetime.now()
        print('execution time:',format(te-ts))
        return function

    return wrapper

@time_this()
def function ():
    print('i am a function ')
    return
