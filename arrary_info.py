numbers = []
"""
print('Enter your Starting point: ')
start = int(input('? '))
print('Enter your Starting point: ')
end_point = int(input('? '))

lists = range(start, end_point + 1)
"""

def even():
    for even in lists:
        if even == 0:
            continue
        if (even % 2) == 0:
            numbers.append(list)
    print(f'This shows an EVEN NUMBERS between {start} and {end_point} is:')
    print(numbers)
    print('The Length of the numbers gotten from the list is: %d' %(len(numbers)))
    numbers.clear()


def odd():
    for odd in lists:
        if odd == 0:
            continue
        if (odd % 2) != 0:
            numbers.append(list)
    print(f'\nThis shows an ODD NUMBERS between {start} and {end_point} is:')
    print(numbers)
    print('The Length of the numbers gotten from the list is: %d' % (len(numbers)))
    numbers.clear()


def double(x):
    return x * 2
# List Comprehension

print([double(x) for x in range(10)])

# Dictionary Comprehension
dict = {i: f'{i*i}' for i in range(10)}
print(dict)

text = 'Life is as, hard as Rock, make, the most, of it, Good Lucks'
vowel = 'ias'

unique_words = {each_letter for each_letter in text if each_letter in vowel}

print('unique_words: %s' %(unique_words))