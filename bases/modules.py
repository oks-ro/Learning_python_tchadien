"""
Mon module
"""

import gzip


pi = 3,14
x = 98
y = 10

def direBonjour(name):
    print("Bonjour", name)


def calculeSomme():
    nbre1 = int(input("Entrer le premier nombre: "))
    nbre2 = int(input("Entrer le deuxième nombre: "))
    return nbre1 + nbre2


def multiplication(a, b):
    return a * b