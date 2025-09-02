from functools import wraps

def logActivity(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        print(f'Calling: {f.__name__}')
        result=f(*args,**kwargs)
        print(f'Finishing: {f.__name__}')
        return result
    return wrapper

@logActivity
def eat(food,sauce='no'):
    print('eating',food,'with sauce?',sauce)

eat('k')