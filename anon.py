class Person:
    name = 'Roy'
    def __init__(self, first_name, last_name): # instance method
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self): # instance method
        print(f'{self.first_name} {self.last_name}')

    def introduce(self): # instance method
        print(f'Hi! I am {self.first_name} {self.last_name}.')

    @classmethod  # class method
    def anonymous(cls):
        return Person('Eyong', 'Roy')
    
cynthia = Person('Cynthia', 'Ibegbu')
# cynthia.get_full_name()
cynthia.introduce()
# another object/instance of the class
ebere = Person('Happiness', 'Ebere')
ebere.get_full_name()
ebere.introduce()

# Anonymous method
anon = Person.anonymous()
anon.introduce()
print(anon.name)