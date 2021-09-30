#!/usr/bin/python3
def uppercase(str):
    for case in str:
        if 97 <= ord(case) <= 122:
            case = chr(ord(case) - 32)
        print("{}".format(case), end="")
    print()
