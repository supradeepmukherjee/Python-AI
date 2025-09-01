class Cup:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size

    def summary(self):
        print(f'{self.type} type of cup of volume {self.size}ml')

cup=Cup('Plastic',180)
cup.summary()