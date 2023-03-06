import random


def passwordGenerator(length=8, type=None):

    upperLetters = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
    lowerLetters = upperLetters.lower()
    special_chars = '!#$%^&*(?/}|{()''""'

    pass1 = random.choices(lowerLetters, k=length)
    pass2 = random.choices(upperLetters, k=length)
    pass3 = random.choices(special_chars, k=length)

    generated_password = ''.join(
        random.choices((pass2 + pass1 + pass3), k=length))

    if type == "u":
        password = "".join(pass2)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        print("___Password Statistics___")
        print("Password: ", password)
        print("Password Lenght: ", length)

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    elif type == "l":
        password = "".join(pass1)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

        print("___Password Statistics___")
        print("Password: ", password)
        print("Password Lenght: ", length)

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    else:
        if length == None or type == None:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            print("___Password Statistics___")
            print("Password: ", generated_password)
            print("Password Lenght: ", length)

            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


passwordGenerator()
