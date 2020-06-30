from functools import wraps

file_path = 'Python Advanced/Decorators/invoke_decorator.txt'

def decorator_argument(name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            with open(file_path, 'a') as fl:
                fl.write(f'{name}, ')
            return f(*args, **kwargs)
        return wrapper
    return decorator

class Container:
    counter = 0
    
    @decorator_argument(name="one")
    def one(self):
        return print('2')

    @decorator_argument(name="two")
    def two(self):
        return print('3')

    @decorator_argument(name="three")
    def tree(self):
        return print('3')

    def call_def(self):
        container.one()
        container.two()
        container.tree()
        container.one()
        container.two()
        container.tree()

container = Container()
container.call_def()
