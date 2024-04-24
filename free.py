"""
Bank name == Afrikmoney

Transactions
Withdrawal
Tranfer
Deposit
Bills

Customer service
Check account balance
Open account
Statement of account
ATM/Cheque 
"""

class Afrikmoney:
    greet = 'Welcome to Afrikmoney'

    def __init__(self, initial_bal=1000,):
        self.initial_bal = initial_bal
        
        
    def open_account(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        while True:
            phone_no = input('Enter your phone number: ')
            if len(phone_no) == 11 and phone_no.isdigit():
                print('✔')
                break
            else:
                print('Invalid phone number.\nPhone number must be 11')                
                continue
            
        address = input('Enter your address: ')
        age = int(input('Enter your age: '))
        if age >= 18:
            print('Proceed to the next step.')
            account_number = phone_no[1:11]
            print(f'Congratulations! {first_name} {last_name}.\nYour account number is {account_number[::-1]}')
        else:
            print("You're not eligile to open account yet.")
            exit()


    def deposit(self):
       amount = int(input('Enter the amount you want to deposit: '))
       current_bal = self.initial_bal + amount
       print(f'Your account has been credited with ${amount}.\nCurrent balance: ${current_bal}')
      

david = Afrikmoney()
tryit = input('Already have an account? Yes or No')
if tryit.capitalize() == 'yes':
    print(david.greet)
    


david.open_account()
david.deposit()