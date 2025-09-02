class C:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size

    @classmethod
    def fromDict(cls,data):
        return cls(data.get('type'),data.get('size'))

    @classmethod
    def fromStr(cls,str):
        type_,size=str.split('-')
        return cls(type_,size)

class Util:
    @staticmethod
    def isValidSize(size):
        return size.lower() in ['small','medium','big']
    
o1=C.fromDict({
    'type':'small',
    'size':'10'
})

o2=C.fromStr('big-50')

o3=C('medium',30)

print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
print(Util.__dict__)
print(Util.isValidSize('MediuM'))