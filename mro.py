# Method Resolution Order

class A:
    label='A Base'

class B(A):
    label='B Derived'

class C(A):
    label='C Derived'

class D(C,B):
    pass

print(D.__mro__)
d=D()
print(d.label)