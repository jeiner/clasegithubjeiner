"""Inicio de decoradores en Python"""


def saludar():
    print("Soy una función")


def superFuncion(funcion):
    funcion()


funcion = saludar

superFuncion(funcion)
