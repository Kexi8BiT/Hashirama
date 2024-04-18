import random
import string


def generate_password(length=16):
    password = ""
    for _ in range(length // 2):
        password += random.choice(string.ascii_letters + string.digits)
    for _ in range(length // 2):
        password += random.choice(string.punctuation)
    parts = [password[i:i + 4] for i in range(0, len(password), 4)]
    password = "-".join(parts)
    password = password.replace("-", ".")

    return password


def regenerate_password(formula, length=False):
    password = ""

    for char in formula:
        if char.isdigit():
            password += str(random.randint(0, 9))
        elif char.isalpha():
            password += random.choice(string.ascii_letters)
        elif char == "!":
            password += random.choice(string.punctuation)
        elif char == " ":
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        else:
            password += char

    # Увеличиваем длину пароля в 2 раза
    if not length:
        password = password + regenerate_password(password, True)

    return password


