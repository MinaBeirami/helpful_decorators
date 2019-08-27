
def n_repeat(n=None):

    def decorator(function):

        def wrapper():
            function()

        return wrapper

    if n:
        for i in range (0,n):
            decorator(n)
        return
    else:
        return decorator

#@n_repeat
@n_repeat()
@n_repeat(4)
def say_cheese():
    print('cheeeeeeeeseeee!')

say_cheese()
