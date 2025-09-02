class Base:
    def __int__(self,type_):
        self.type=type_

class Derived(Base):
    def __init__(self,type_,level):
        # Base.__init__(type_)
        super().__init__()
        self.level=level