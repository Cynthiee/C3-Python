import random
import math 

print(random.randrange(1, 4))


#Explicit conversion
float_string = '56.7'
print(float_string)
print(type(float_string))
converted = float(float_string)
print(converted)
print(type(converted))

new_int = int(converted)
print(new_int)



# print(type(int(float_string)))


x = 3.6 + 3
print(round(x))
print(str(x))


m = 8
n = 4.1
print(m + n)
# print(int(m+n))


20 
"67"
print(20)
j = 300
k = 89
print(id(j))
print(id(k))


for i in range(128):
    print(f"ASCII value: {i}, Character: {chr(i)}")