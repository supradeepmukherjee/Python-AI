menu={
    'masala':10,
    'ada':15
}

try:
    menu['skfnjdfdf']
except:
    print('Key does not exist cant you see')

def serve(flavor):
    try:
        print('preparing',flavor)
        if flavor=='no':
            raise ValueError('ok no flavor')
    except ValueError as e:
        print('Error: ',e)
    else:
        print(flavor,'served')
    finally:
        print('final')

serve('bfdj')
serve('no')