<<<<<<< HEAD
from os.path import realpath, dirname, join
import re
def JeSpecSymbol(s:str):
    if s.isdigit() == True or s == ".":
        return False
    else:
        return True
def parse(s:str):
    cis:list = []
    zna:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        soubor:list = file.read().split('\n')
        idxr: int = 0
        for x in soubor:
            c = re.search("([0-9]+)",x)
            if re.search("([0-9]+)",x) != None:
                cis.append([(idxr,c.span()[0]),(idxr,c.span()[1]),c.group()])
            z = re.search("[^0-9\.]",x)
            if re.search("[^0-9\.]",x) != None:
                zna.append([(idxr,z.span()[0]),(idxr,z.span()[1])])
            idxr += 1
        sx:str = ""
        print(cis)
        print(zna)
        soucet:int = 0
        #for zac,kon,c in cis:

            #print("radek:"+str(zac[0])+"zacatek:"+str(zac[1])+"konec:"+str(kon[1])+"cislo:"+c)


parse("test.txt")
=======
from os.path import realpath, dirname, join
import re
def JeSpecSymbol(s:str):
    if s.isdigit() == True or s == ".":
        return False
    else:
        return True
def parse(s:str):
    cis:list = []
    zna:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        soubor:list = file.read().split('\n')
        idxr: int = 0
        for x in soubor:
            c = re.search("([0-9]+)",x)
            if re.search("([0-9]+)",x) != None:
                cis.append([(idxr,c.span()[0]),(idxr,c.span()[1]),c.group()])
            z = re.search("[^0-9\.]",x)
            if re.search("[^0-9\.]",x) != None:
                zna.append([(idxr,z.span()[0]),(idxr,z.span()[1])])
            idxr += 1
        sx:str = ""
        print(cis)
        print(zna)
        soucet:int = 0
        #for zac,kon,c in cis:

            #print("radek:"+str(zac[0])+"zacatek:"+str(zac[1])+"konec:"+str(kon[1])+"cislo:"+c)


parse("test.txt")
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
