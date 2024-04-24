class Person:
    def __init__(self, name, age, height, gender, complexion):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.complexion = complexion

if __name__ == '__main__':
    chi = Person('Chioma', '20yrs', '170cm', 'F', 'fair')
    print(f'{chi.name}, {chi.age}, {chi.height}, {chi.gender}, {chi.complexion}')

        