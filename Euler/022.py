
def result(content):
    total = 0

    # receive (id, name) from the list
    for id, name in enumerate(content):
        for char in name:
            # ord(char)-ord('A')+1  -->  get letter Unicode where A=1, B=2, etc.
            # id + 1 since id starts at 0
            total += (id + 1) * (ord(char)-ord('A')+1)
    return total

try:
    nameFile = open("p022_names.txt")
    # reads file
    content = nameFile.read()
    nameFile.close()
    # fomats the contents of the file into a list and sorts it
    nameList = sorted(content.replace('"','').split(','))
    print(result(nameList))
except IOError:
    nameFile.close()

