class Leaf:
    def __init__(self,age):
        self._age=age

    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,a):
        if 1<=a<=5:
            self._age=a
        else:
            raise ValueError('Age must be between 1 & 5')
        
leaf=Leaf(9)
print(leaf.age)
leaf.age=9