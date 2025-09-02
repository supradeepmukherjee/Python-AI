class Base:
    def __init__(self,type_):
        self.type=type_

    def prepare(self):
        print(f'Preparing {self.type} type')

class Derived(Base):
    def add(self):
        print('Adding')

class Other:
    b=Base
    
    def __init__(self):
        self.x=self.b('T')

    def test(self):
        print('Type',self.x.type)
        self.x.prepare()

class Check(Other):
    b=Base

other=Other()
check=Check()
other.test()
check.x.prepare()