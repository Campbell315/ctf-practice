#!/usr/bin/env python3
import string

def ASCIIdecrypt(file):
    flag = []


    with open(file) as target:
        contents = target.read()
        numbers = [int(val) for val in contents.split()]
        for value in numbers:
            initial = value % 37

            if initial in range(26):
                flag.append(string.ascii_uppercase[initial])
            elif initial in range(26, 36):
                flag.append(string.digits[initial - 26])
            else:
                flag.append("_")

# include flag template
    print("".join(flag))


#test
ASCIIdecrypt("../../pico/cryptography/message.txt")