def print_number(n):
    if n % 2 == 0:
        print('Number {} is even'.format(n))
    else:
        print('Number {} is odd'.format(n))

# Get user input and convert it to an integer
try:
    user_input = int(input('Enter your number: '))
    print_number(user_input)
except ValueError:
    print('Please enter a valid number.')

