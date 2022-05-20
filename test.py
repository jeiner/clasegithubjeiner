def funcion_cadena():
    cadenaIn = input("Ingresar cadena de caracteres: ")
    i = 0
    for x in cadenaIn:
        i = i + 1
    print(i)

    var = cadenaIn.split()
    print(len(var))

funcion_cadena()