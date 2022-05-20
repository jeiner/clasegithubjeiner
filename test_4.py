

def fileManipulation(name, mode):

    try:
        file = open(name, mode)
        print(file.read())
        return file
    except OSError as err:
        print("Error de lectura: {}".format(err))


fileWrite = "my_files/file.txt"
fileAppend = "my_files/append.txt"

print("Lectura de un archivo no existe")
fileManipulation(fileWrite, "r")


"""
Manejo de archivos en Python:

r: Lectura de archivos

w: Escrituras líneas en nuestro archivo

a+: Escritura de nuevas líneas en nuestro archivo

close(): Función que borra el búfer de memoria y cierra nuestro archivo aperturado.

"""
