##!/usr/bin/python3

# Exercício 3.1


def right_justify(s):
    extra = 70 - len(s)
    justified = (extra * ' ' + s)
    print(justified)


#right_justify("Bulls on parade")


# Exercício 3.2


def do_twice(f, a):
    f(a)
    f(a)


def print_spam():
    print('spam')


def print_twice(bruce):
    print(bruce)
    print(bruce)


def print_once(v):
    print(v, end='')


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


def do_four_b(f):
    f()
    f()
    f()
    f()


def print_four(v):
    print(v, end='')
    print(v, end='')
    print(v, end='')
    print(v, end='')


# do_four('chris')
# do_twice(print_twice, 'spam')


# Exercício 3.3


def desenhar_grade():
    line1 = '+ - - - - '
    line2 = '|         '
    print_four(line1 * 4 + '+\n' + ((line2 * 4 + '|' + '\n') * 4))
    print(line1 * 4 + '+')



desenhar_grade()
    





