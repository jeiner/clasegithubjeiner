
tecnlogiasBackend = ["\nPython", "Java", "php", "Ruby", "NodeJS\n"]

tecnlogiasFrontend = ["\nJavaScript", "Angular", "ReactJS", "Boostrap"]

fileExample = open("my_files/file.txt", "a+")

fileExample.writelines(tecnlogiasBackend)

fileExample.writelines(tecnlogiasFrontend)

fileExample = open("my_files/file.txt", "r")

print("Nuestro contenido del file es: ", fileExample.read())
