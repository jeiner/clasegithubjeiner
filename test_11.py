"""Uso de decoradores con *args y **kwargs"""


def funcionA(funcionB):
    def funcionC(*args, **kwargs):
        print("Antes de la ejecucion  de la funcion a decorar")

        resultado = funcionB(*args, **kwargs)  #Comprime los parámetros que pueda necesitar la función

        print("Después de la ejecución de la función a decorar")

        return resultado

    return funcionC


#@funcionA
def suma(a, b, c):
    s = a + b + c
    return print(s)


decorador = funcionA(suma)
decorador(50, 90, 100)
