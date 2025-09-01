from functools import wraps

def myDecorator(f):
    @wraps(f)
    def wrapper():
        print("Before function runs")
        f()
        print("After function runs")
    return wrapper

@myDecorator
def greet():
    print("Hello from decorators class")

greet()
print(greet.__name__)