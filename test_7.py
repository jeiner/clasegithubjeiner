

tecnlogiasBackend = ["\nPython", "NodeJS\n"]

fileExample2 = open("my_files/file.txt", "a+")

fileExample2.writelines(tecnlogiasBackend)

fileExample2 = open("my_files/file.txt", "r")

for newLine in fileExample2:
    print(newLine)

fileExample2.close()
