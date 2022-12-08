# this is just a few ways function works
# function without argument
def sayHello():
    return "hello"

print(sayHello())

# function with argument
def saySomething(something):
    return "you just typed: " + something

print(saySomething("well well well"))

# **kwargs
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

# *args
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

for i in inclusive_range(25):
    print(i, end = ' ')
print()
