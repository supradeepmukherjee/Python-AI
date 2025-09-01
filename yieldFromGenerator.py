def desiChai():
    yield "Darjeeling"
    yield "Assam"

def foreignChai():
    yield "toxic"
    yield "adulterated"

def full():
    yield from desiChai()
    yield from foreignChai()

for chai in full():
    print(chai)

def stall():
    try:
        while True:
            order=yield "Waiting for new order"
    except:
        print('Stall closed')

dokan=stall()
print(next(dokan))
dokan.close()