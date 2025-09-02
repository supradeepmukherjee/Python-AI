def processOrder(item,qty):
    try:
        price={'masala':20}[item]
        print('Total cost is: ',price*qty)
    except KeyError:
        print('sorry not in menu')
    except TypeError:
        print('qty must be no.')

processOrder('ginger',2)
processOrder('masala','two')