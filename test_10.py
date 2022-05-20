"""Decoradores en Python"""

"""Creamos nuestro decorador"""


def funcionA(funcionB):
    def funcionC():
        print("Antes de ejecutar la función a decorar")

        funcionB()

    return funcionC()


"""Creamos nuestra funcion a decorar"""


@funcionA
def saludar():
    print("Hola Pythonistas")


