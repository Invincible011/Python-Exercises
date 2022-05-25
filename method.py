from datetime import datetime

now = int(datetime.now().strftime('%Y'))
# This will print 2022

print('Enter your name: ')
name = input('? ')
print('Enter your Date of Birth: ')
dob = int(input('-> '))

age = now - dob

def greet(local: str):
    print(f'Good Afternoon Dear\nHow are you {local}?')
    if age > 0:
        return f'I know your age, your age is: {age}'
    else:
        return f'Your age {age} is invalid'


#  Parameter is defined inside a function while Argument is defined when a function is revoked.
#  is_adult(name): -> This is called an ARGUMENT.
#  print(is_adult("Ohinoyi")) -> This is called a PARAMETER.

def is_adult():
    if age < 18:
        return f'With your current age {age}, you are still under age.'
    else:
        return 'You are an Adult.'

print(greet(name))
print(is_adult())