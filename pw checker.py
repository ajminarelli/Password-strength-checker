#Password strength checker program to evaluate the strength of your password and give feedback.

password = input('Enter your password: ')
common_passwords = {
    '123456',
    '111111',
    'admin',
    'qwerty',
    'password',
    '123456789',
    '12345'
}

if password in common_passwords:
    print('This password is commonly used and insecure. Please enter a different password.')
    exit()



def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password
               )
def check_digit(password):
    return any(char.isdigit() for char in password)

def check_specials(password):
    special_char = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
    return any(char in special_char for char in password)

checks = {
    'Length >= 8': check_length(password),
    'An uppercase letter': check_uppercase(password),
    'A lowercase letter': check_lowercase(password),
    'Digits': check_digit(password),
    'A special character': check_specials(password),
}

score = sum(checks.values())

if score == 5:
    print('Your password is very strong!')
elif score == 4:
    print('Your password is strong!')
elif score == 3:
    print('Your password is mediocre.')
elif score == 2:
    print('Your password is weak.')
elif score == 1:
    print('Your password is very weak.')


feedback_messages = {
    'Length >= 8': 'Your password is too short. Use at least 8 characters to make it more secure.',
    'An uppercase letter': 'Add an uppercase letter (A-Z) to increase complexity.',
    'A lowercase letter': 'Add a lowercase letter (a-z) to make it harder to guess.',
    'Digits': 'Add a digit to increase complexity.',
    'A special character': 'Add a special character to make it harder to guess.'

}


if score == 5:
    print('No further improvements required.')
else:
    for criterion, passed in checks.items():
        if not passed:
            print(feedback_messages[criterion])
