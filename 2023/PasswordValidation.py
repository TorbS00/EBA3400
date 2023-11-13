# Password

def length_check(password):
    password_length = len(password)
    if not (6 <= password_length <= 12):
        return False
    return True


def uppercase_check(password):
    if not length_check(password):
        return False
    for char in password:
        if char.isupper():
            return True
    return False


def upper_case1(char):
    return char.isupper()


def digit_check(password):
    if not uppercase_check(password):
        return False
    for char in password:
        if char.isdigit():
            return True
    return False


def special_character_check(password):
    if not digit_check(password):
        return False
    special_characters = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?")
    for char in password:
        for special_char in special_characters:
            if special_char in char:
                return False
    return True


def password_validator(password):
    if not special_character_check(password):
        print("Invalid password")
        return
    print("Valid password")


password_validator(input("Enter password:"))
