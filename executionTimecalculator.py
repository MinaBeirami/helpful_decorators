

from datetime import datetime,timedelta,time

"""
    third-version
    simple decorator to measure execution time of a function.
"""

def decorator(*unit):

    def wrapper(function):

        tic=datetime.now().time().microsecond
        #print(tic)
        toc=datetime.now().time().microsecond
        #print(toc)
        time=toc-tic
        #print(unit)

        if type(unit) == tuple and len(unit):
            if unit[0] == 'micros':
                print('this function took ' ,time,'microsecond')
            elif unit[0] == 'milis':
                time=time/1000
                print('this function took ',time,' mili second')
            elif unit[0] == 's':
                time=time/1000000
                print('this function took ',time,' second')
        else:
            print( 'this function took ',time,' micro second')
        return function
    return wrapper

@decorator()
@decorator('milis')
@decorator('micros')
@decorator('s')
def function():
    #print ("i am function")
    return 'i am a function'


