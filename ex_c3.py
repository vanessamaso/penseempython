##!/usr/bin/python3

# Exercício 3.1


def right_justify(s):
    extra = 70 - len(s)
    justified = (extra * ' ' + s)
    print(justified)


right_justify("Bulls on parade")
