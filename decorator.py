"""def start_end_decorator(func):
    
    def wrapper(*args, **kwargs):
        print('Start')

        func(*args, **kwargs)
        print('End')
    return wrapper

@start_end_decorator
def print_name():
    print('alex')

#print_name = start_end_decorator(print_name)

print_name()

@start_end_decorator
def add5(x):
    return x+5

result = add5(10)

print(help(add5))

print(add5.__name__)

print(result)"""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)

def require_auth(func):
    def wrapper(*args, **kwargs):
        user_authenticated = True  # Simulate authentication
        if not user_authenticated:
            print("Access denied!")
            return
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_dashboard():
    print("Welcome to the dashboard!")

view_dashboard()

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()