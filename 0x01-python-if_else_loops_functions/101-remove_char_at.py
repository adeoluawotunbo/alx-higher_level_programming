#!/usr/bin/python3
def remove_char_at(str, n):
    remove_char = 0
    nthing = ""
    for character in str[:]:
        if remove_char != n:
            nthing += character
            remove_char += 1
    return nthing
