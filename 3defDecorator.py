

from datetime import datetime
"""
    second-version
    3 callables inside each other.
    first callable (wrapper) take  arguments of a callable(here is the callable
    is "function")
    second callable(decorated) takes a callable( here the callable is
    "wrapper")
    third callable (decorator) takes a callable(callable) (here the callable->
    callabe is decorated(wrapper) )

"""

def decorator(unit=None):

    def decorated(function):

        def wrapper():

            tic=datetime.now().time().microsecond
#            print(tic)
            function()
            toc=datetime.now().time().microsecond
#            print(toc)
            time=toc-tic
#            print(unit)
            print (time,'micro second.')
        return wrapper

    if callable(unit):
        return decorated(unit)
    else:
        return decorated

@decorator
@decorator()
@decorator('ms')
def function():
    print ("i am function")

function()
