# grade = float(input('Enter your score: '))

# if grade >= 75 and grade <= 100:
#     print(f'Excellent! Your score is {grade}. You got an A.') 
# elif grade >= 60 and grade <= 74:
#     print('Awesome! Your scored is B')
# elif grade >= 50 and grade <= 59:
#     print('Good! You got a C')
# elif grade >= 40 and grade <= 49:
#     print('Fairly good! You got a D')
# elif grade >= 30 and grade <= 39:
#     print('Narrow escape.You got an E')
# elif grade >= 0 and grade <= 34:
#     print('Poor! You got an F')
# else:
#     print('Invalid score.\nInput a valid score!')
   
# a = 20
# b = 689

# if a > b:
#     print('b is greater than a')
# else:
#     print('a is less than b')


# Check for Even or Odd Numbers

# if number % 2 == 0:
#     print(f'{number} is even number!')
# else:
#     print(f'{number} is odd number!')



# # Write a program that checks if the user
# # eligible to vote
    

# if age >= 18:
#     print("You're eligible to vote.")
#     print('You are an adult')
# else:
#     print('You\'re not eligible to vote.')
    
# # Create a program that checks if a number is
# # positive, negative or zero 
    
# num = float(input('Enter any number: '))

# if num > 0:
#     print(f'{num} is a positive number.')
# elif num < 0:
#     print(f'{num} is a negative number.')
# else:
#     print('Zero')


# # Shorthand If or one line if statement
# # if condition: statement_1; statement_2
    
# if age >= 18: print("You're an adult")
# else: print('You\'re a child')

#Tenary operator
# statement condition else statement
number = int(input('Enter a number: '))

even_or_odd = 'Even' if number % 2 == 0 else 'Odd'
print(even_or_odd)

age = int(input('Enter your age: '))

eligible_or_not = 'Eligible' if age >= 18 else 'Not eligible'
print(eligible_or_not)