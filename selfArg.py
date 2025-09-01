class Cup:
    size=150
    def describe(self):
        return f'Volume: {self.size}ml'

cup=Cup()
print(cup.describe())
print(Cup.describe(cup))

cup2=Cup()
cup2.size=100
print(Cup.describe(cup2))