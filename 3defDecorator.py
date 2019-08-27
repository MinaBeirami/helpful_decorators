from datetime import datetime

'''
    second-version
    3 callables inside each other.
    first callable (wrapper) take  arguments of a callable(here is the
    callable is "function")
    second callable(decorated) takes a callable( here the callable is
    "wrapper")
    third callable (decorator) takes a callable(callable) (here the callable->
    callabe is decorated(wrapper) )
'''

def time_this(unit=None):

    def decorator(function):

        def wrapper():
            tic = datetime.now().time().microsecond
            function()
            toc = datetime.now().time().microsecond
            time = toc - tic
            print(time, 'micro second.')
        return wrapper

    if callable(unit):
        return decorator(unit)
    else:
        return decorator

@time_this
#@time_this()
#@time_this('ms')
def function():
    print ("i am function")

function()

