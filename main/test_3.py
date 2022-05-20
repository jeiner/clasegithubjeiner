

"""Manejo de Archivos"""
"""Lectura de archivos"""

fileExample = open("../my_files/file.txt", "r")

print("Contenido de nuestro archivo: ", fileExample.read())

fileExample.close()
