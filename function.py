#def func(a,b, *args, **kwargs):
def func(*args, a, b):
    print(a,b)
    for i in args:
        print(args)
    for key in kwargs:
        print(key, kwargs[key])

#func(1,2,3,4,5, six = 6, seven = 7)

func(1, 2, 3, 4)