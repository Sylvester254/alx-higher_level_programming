#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) != 'q' and chr(alphabet) != 'e':
        print("{}".format(chr(alphabet)), end="")
# The ASCII value of the lowercase alphabet is from 97 to 122.
# chr() function returns the character that represents the specified unicode.
