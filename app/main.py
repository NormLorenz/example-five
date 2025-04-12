# This is a simple Python script that prints a greeting message with the user's name and age.
# The script uses f-strings for string formatting, which is a convenient way to embed expressions inside string literals.

''' This is the main entry point '''
def main():
    name = 'John Doe'
    age = 30
    print(f'Hello, my name is {name} and I am {age} years old.')


def junk():
    print(f'Hello')


def add(x: int, y: int) -> int:
    """Returns the sum of x and y."""
    return x + y


if __name__ == "__main__":
    main()
