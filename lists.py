fruits = ['mango', 'orange', 'pineapple', 
          'banana', 'apple', 'guava', 
          'pear', 'watermelon']
print(fruits)
fruits[5:7] = ['grapes']
print(fruits)
if 'Mango' not in fruits:
    print('Yippie!!')



cars = list(('G-wagon', 'Ferarri', 'Chevrolet', 'Bullion van', 
             'Tesla', 'Rolls Royce', 'IVM', 'Lamborghini', 'Lexus', 
             'Benz', 'BMW', 'Tundra', 'Audi'))
print(cars)
print("--------------------------")
print(cars[6])
print(cars[:-4])
print(cars[2:8])
cars.insert(3, 'Fisker')
print(cars)

cars.append('Sequoia')
print(cars)
print('*****************************************************')
# fruits.extend(cars)
# print(fruits)

thistuple = ('Aba', 'Oweeri', 'Enugu')
fruits.extend(thistuple)
print(fruits)
fruita = [1,2, 3, (4, 5, 6)]
print(fruita)

hairs = ['Bone straight', 'Pixie curl', 'Braided wig', 'Bob wig', 
         'Barbie', 'SDD Vietnam bone straight', 'Full frontal wig', 'Pony tail', 'Skullcap']
print(hairs)
hairs.remove('Barbie')
print(hairs)
hairs.pop(2)
print(hairs)
hairs.pop()
print(hairs)
del hairs[-1]
print(hairs)

hairs.clear()
print(hairs)

