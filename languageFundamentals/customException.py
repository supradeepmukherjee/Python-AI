class OutOfIngredientsError(Exception):
    pass

def make(milk,sugar):
    if milk==0 or sugar==0:
        raise OutOfIngredientsError('Milk or Sugar')

make(1,0)