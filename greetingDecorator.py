
def greeting():
    def wrapper (function):
        print ('Hello')
        fname,lname=function()
        print('welcome',fname,lname)
    return wrapper

@greeting()
def function ():
    fname=input("firs name: ")
    lname=input("last name: ")
    return fname,lname

