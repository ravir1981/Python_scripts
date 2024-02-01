password = input("Enter the password:")


def strength(password):
    result = {}

    if len(password) > 8:
        result['lenth'] = True
    else:
        result['lenth'] = False

    upper = False
    for character in password:
        if character.isupper():
            result['upper'] = True

    for character in password:
        if character.isdigit():
            result['digit'] = True
        else:
            result['digit'] = False

    print(result)

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


message = strength(password)
print(message)