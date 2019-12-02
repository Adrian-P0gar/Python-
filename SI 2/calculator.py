import os
import math
import string


def calc():
    try:
        a = int(input("Hello! Enter a number! (or a letter to exit)"))
        b = int(input('Enter another number:'))
    except ValueError:
        exit()

    operation = input('Enter a operation:')

    if operation == ("+"):
        print(int(a) + int(b))
    elif operation == ("-"):
        print(int(a) - int(b))
    elif operation == ("*"):
        print(int(a) * int(b))
    elif operation == ("/"):
        print(int(a) / int(b))
    else:
        exit()


i = 1
while i == 1:

    calc()
