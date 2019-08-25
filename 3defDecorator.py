

from datetime import datetime
"""
    second-version
    3 callables inside each other.

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
