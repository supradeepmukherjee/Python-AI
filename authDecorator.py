from functools import wraps

def requireAdmin(f):
    @wraps(f)
    def wrapper(role):
        if role!='admin':
            print('Access Denied')
        else:
            return f(role)
    return wrapper

@requireAdmin
def accessInventory(role):
    print('Access granted to tea inventory')

accessInventory('user')
accessInventory('admin')