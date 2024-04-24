class Eyong:
    message = "Welcome to Eyong's family "
    name = input("Enter your name: ")
       
    print('Hello', name)
    print(message)
   
    def complexion(self, color):
        print(f'I am {color}')

    def height(self):
        heigth = ('Enter your height: ')
        print('I am {} tall'.format(heigth))

    
roy = Eyong()
roy.complexion('Dark')
roy.height()