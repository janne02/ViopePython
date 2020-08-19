import time

def readfile(name):
    try:
        readfile = open(name,'r')
        content = readfile.read()
        readfile.close()
        return content
    except IOError:
        return False
def addfile(name, uinput):
    try:
        uinput = uinput+":::"
        uinput += time.strftime("%X %x")
        addfile = open(name,'a')
        addfile.write(uinput+"\n")
        addfile.close()
    except IOError:
        return False
def emptyfile(name):
    try:
        emptyfile = open(name,'w')
        emptyfile.close()
    except IOError:
        return False 

while True:
    selection=input('''(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta
Mitä haluat tehdä?: ''')
    if selection=='1':
        content=readfile("notebook.txt")
        print(content)
    if selection=='2':
        uinput=input("Kirjoita uusi merkintä: ")
        addfile("notebook.txt",uinput)
    if selection=='3':
        emptyfile("notebook.txt")
        print("Muistio tyhjennetty.")
    if selection=='4':
        print("Lopetetaan.")
        break
