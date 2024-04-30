a = 22
try:
    print(a)
except NameError:
    print('Variable "a" is not defined')
else:
    print('No error occured')
finally:
    print('Done')


# raise keyword to throw an error

x = -1
# if x < 0:
#     raise Exception('x is less than 0')

# b = "12"
# if b is not x:
#     raise TypeError('Cannot add string and integer')

try:
    if a == c:
        print('Hello')
except:
    print('Indentation error')