
"""Leer especificamente un línea de mi file o archivo"""

fileExample = open("my_files/file.txt", "r")

print(fileExample.readline())

print(fileExample.readline(10))

print(fileExample.readline(40))

print(fileExample.readline(14))

fileExample.close()
