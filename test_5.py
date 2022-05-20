

fileExample = open("my_files/file.txt", "w")

fileExample.write("Python es un lenguaje multiplataforma\n")
fileExample.write("Python está basado en POO.\n")
fileExample.write("Python basado en diferentes paradigmas de programación")

fileExample = open("my_files/file.txt", "r")

print("Nuestro file tiene el siguiente contenido: ", fileExample.read())
