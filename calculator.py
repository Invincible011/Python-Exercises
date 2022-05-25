# Creating a user defined FUNCTION that will be usage in another program

# Read about Terminal and Vim fundamentals
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    try:
        return x / y
    except:
        f'{y} is not divisible by {x}, {y} is either Zero or Negative variable'
    # return x / y

def multiply(x, y):
    return x * y

def power(x, y):
    return x ** y

# print(f'Addition: {add(10, 5)}')
# print(f'subtract: {subtract(20, 5)}')
# print(f'divide: {divide(10, 2)}')
# print(f'multiply: {multiply(10, 5)}')
# print(f'power: {power(10, 2)}')

text = 'I Love you so much Raihanat'

add = [text.split() for i in text]

print(len(text))
print(len(add))
print(add)

import streamlit as st