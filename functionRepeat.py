def repeat_twice(function):
    def wrapper():
        print('this is first call of function:',function.__name__)
        function()
        print('this is second call of function:',function.__name__)
        function()
    return wrapper


@repeat_twice
def say_cheese():
    print('cheeeeeeeeseeee!')

say_cheese()

