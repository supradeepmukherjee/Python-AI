class InvalidChaiError(Exception):pass

def bill(flavor,cups):
    menu={'masala':20,'ada':40}
    try: 
        if flavor not in menu:raise InvalidChaiError('not available')
        if not isinstance(cups,int):raise TypeError('Number of Cups must be integer')
        print(f'Your bill for {cups} cups of {flavor} flavor is {menu[flavor]*cups}')
    except Exception as e:
        print('Error: ',e)

