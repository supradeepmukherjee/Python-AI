def chaiCustomer():
    print('Welcome')
    order=yield
    while True:
        print(f"Preparing {order}")
        order=yield

stall=chaiCustomer()
next(stall) # starting the generator

stall.send('Masala Chai')
stall.send('Lemon Chai')