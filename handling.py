import os
# with open('C:/Users/islac/Documents/hello.txt', 'r') as b:
#     data = b.readlines()
#     print(data)

# with open('filename','mode') as f:

with open('none.txt', 'w') as f:
    data = 'Writing into a file that does not exist'
    f.write(data) 


with os.scandir('C:/Users/islac/Desktop/Documents') as entries:
    for entry in entries:
        print(entry.name)