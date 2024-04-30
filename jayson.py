import json
car ={
    'brand':'Toyota',
    'model': 'Spider',
    'year': 2020,
    'color': ['ash', 'red', 'black'],
    'color': ['ash', 'red', 'black', 'blue']}

new_car = json.dumps(car, indent=1, separators=('*', '='), sort_keys=True)
print(type(new_car))
print(new_car)
# json_car = json.loads(new_car)
# print(json_car)
# print(type(json_car))


hairs = ['Bone straight', 'Pixie curl', 'Braided wig', 'Bob wig', 
         'Barbie', 'SDD Vietnam bone straight', 
         'Full frontal wig', 'Pony tail', 'Skullcap']

new_hair = json.dumps(hairs, indent=2)
print(new_hair)