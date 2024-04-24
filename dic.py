car ={
    'brand':'Toyota',
    'model': 'Spider',
    'year': 2020,
    'color': ['ash', 'red', 'black'],
    'color': ['ash', 'red', 'black', 'blue']
}
print(car)
print(car['brand'])
print(car.get('color'))
print(car.keys())
car['year'] = 2023
print(car)
print(car.values())
print(car.items())

if 'color' in car:
    print(True)

car.update({'engines':'v6'})
# print(car)
# car.pop('color')
# print(car)
# car.popitem()
# print(car)
# car.clear()
# print(car)

# loop through keys
for x in car:
    print(x)

# loop through values
for x in car:
    print(car[x])

for c in car.values():
    print(c)

for y in car.keys():
    print(y)

for i in car.items():
    print(i)

carr = {'brands':'Lexus'}
carr = car.copy()
print(carr)

cars = dict(carr)
print(cars)

python_class = {
    'student1':{
        'name': 'John',
        'age': 17,
        'course': 'Ethical hacking',
        'complexion': 'caramel'
    },
    'student2':{
        'name': 'Mummy Happy',
        'age': 40,
        'course': 'Data Science',
        'complexion': 'dark'
    },
      'student3':{
        'name': 'Justice',
        'age': 12,
        'course': 'AI/ML',
        'complexion': 'fair'
    },
      'student4':{
        'name': 'Ifeanyi',
        'age': 11,
        'course': 'Cybersecurity',
        'complexion': 'fair'
    },
      'student5':{
        'name': 'Rejoice',
        'age': 14,
        'course': 'Cybersecurity',
        'complexion': 'dark'
    },
      'student6':{
        'name': 'Chigaemezu',
        'age': 6,
        'course': 'Marketing',
        'complexion': 'caramel'
    },
      'student7':{
        'name': 'Roy',
        'age': 22,
        'course': 'Money',
        'complexion': 'caramel'
    },
}

print(python_class.items())

for x in python_class.items():
    print(x)