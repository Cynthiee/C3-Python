# num = '10'
# num1 = 10
# print(num)
# print(num1)
# print(type(num))
# print(type(num1))

# Builtin Data Types
# str
fruit = 'Mango'
print(fruit)
print(type(fruit))

# int
number = 40
print(number)
print(type(number))

# float
float_num = 23.4
print(float_num)
print(type(float_num))

# Complex
complex_num = 23j
print(complex_num)
print(type(complex_num))

# list
cars = ['G-wagon', 'Audi', 'Tayota', 'Tesla', 'Lamborghini', 'Rolls Royce', 'IVM']
print(cars)
print(type(cars))

# tuple
afro_beats_artists = ('Burna Boy', 'Lyta', 'Fireboy', 'Davido', 'Wizkid')
print(afro_beats_artists)
print(type(afro_beats_artists))

# range
range_num = range(8)
print(range_num)
print(type(range_num))


# Dictionary
student_info = {'name':'Cynthia',
                'age':'50',
                'stack':'Python',
                'level':'Entry'}

print(student_info)
print(type(student_info))

# set
cooking_set = {'Knife', 'Plate', 'Plate', 'Spoon', 'Pot', 'Stove'}
print(cooking_set)
print(type(cooking_set))

# frozenset
frozen_set = frozenset({1,2,3,4,5,6,7,8,9,10})
print(frozen_set)
print(type(frozen_set))

# boolean
a = True
print(a)
print(type(a))
b = False
print(b)
print(type(b))

# bytes
x = b'Hello'
print(x)
print(type(x))

y = bytearray(5)
print(y)
print(type(y))

z = memoryview(bytes(5))
print(z)
print(type(z))

none_type = None
print(none_type)
print(type(none_type))

floating_num = 455.
print(floating_num)
print(type(floating_num))

f = 35e4
print(f)
g = 12E3
print(g)
h = -674.34e13
print(h)

print(3j + 5)

print(4/2)



num1 = 45
num2 = 23.90
print(float(num1 + num2))
print(int(num2))
print(complex(num1))

def greet():
    print('Hello World')

greet()
