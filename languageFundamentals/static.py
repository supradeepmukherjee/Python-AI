class C:
    @staticmethod
    def clean(text):
        return [i.strip() for i in text.split(',')]
    
# o=C()
print(C.clean('  bfsjfvjfd, dfhbf, hsbdhfsdbfj     ,  '))