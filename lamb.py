# lambda is a keyword used to write function
# syntax
# variable = lamda parameter :  return statement
# call the function
greet = lambda : 'Hello'
print(greet())

# holiday = lambda a : a.strip().upper()
# print(holiday(input("")))

party = lambda b, c, d : print(b + c * d)
party(20, 40, 21)


sort_it = [2,4,1,6,7,5,9]
g = sorted(sort_it, key=lambda x: abs(x))
print(g)

h = lambda y : y **2
print(h(2))
print(h(4))
print(h(6))
print(h(8))

def add(n):
    return lambda a : a + n

addition = add(7)
print(addition(8))

# def name(name):
#     def sex(age):
#         return name, age

# name_of = name('Cynthia')




