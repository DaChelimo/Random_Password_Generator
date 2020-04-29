import string
import random

num = int(input("How long would you like your password to be: "))
password = ""


def generator(num):
    global password
    for i in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
    print(password)


generator(num)