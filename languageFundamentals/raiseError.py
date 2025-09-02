def drink(flavor):
    if flavor not in ['masala','ginger','elaichi']:
        raise ValueError('Not available')
    print('drinking',flavor)

drink('fgbhd')