
def n_repeat(n = 1):

    def decorator(function):

        def wrapper():
            counter = n
            while counter != 0:
                counter = counter - 1
                function()
        return wrapper
    return decorator

@n_repeat
@n_repeat()
@n_repeat(4)
def say_cheese():
    print('cheeeeeeeeseeee!')

say_cheese()

