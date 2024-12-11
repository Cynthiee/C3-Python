import os

# os.remove('none.txt')
if os.path.exists('file.txt'):
    os.remove('file.txt')
else:
    print('Removed')
