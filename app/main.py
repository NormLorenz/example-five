# This is a simple Python script that prints a greeting message with the user's name and age.
# The script uses f-strings for string formatting, which is a convenient way to embed expressions inside string literals.

import random

''' This is the main entry point '''
def main():
    x = 3
    print(random.randrange(1, 100) + x)

    a = '''Lorem ipsum dolor sit amet, clut labore et dolore magna aliqua.'''
    print(a)
    print(a[6])
    for b in a:
        print(b)
    print(len(a))
    print('magna' not in a)

def junk():

    name = 'John Doe'
    age = 30
    print(f'Hello, my name is {name} and I am {age} years old.')

def junk():
    print('This is a junk function that does nothing.')

def add(x, y):
    """Returns the sum of x and y."""
    return x + y


if __name__ == "__main__":
    main()
