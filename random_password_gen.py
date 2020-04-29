import string
import random

num = str(input("How long would you like your password to be (e.g 14) : "))
num = num.strip()
num = int(num)
password = ""


def generator(num):
    global password
    for i in range(num):
        x = random.randint(0, 94)
        password += string.printable[x]
    print(password)


generator(num)