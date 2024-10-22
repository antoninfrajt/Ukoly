from os.path import realpath, dirname, join
def pocitej(c:list)->int:
    s:int = 0
    for i in range(0,256):
        slot = 1
        for x in c:
            if hash(x[0]) == i:
                #print(x[0])
                s += (i+1)*slot*x[1]
                slot += 1
                #print(s)
    return s
def hash (s:str)->int:
    kod:int = 0
    for x in s:
        kod += ord(x)
        kod = kod*17
        kod = kod % 256
    return kod
def parse(s:str):
    soucet:int = 0
    cocky:list = []
    labels:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split(',')
            for x in soubor:
                #print(x)
                if x[-2] == "=":
                    doc = list([x[:-2],int(x[-1])])
                    if x[:-2] not in labels:
                        cocky.append(doc)
                        labels.append(x[:-2])
                    else:
                        for i in range(0,10):
                            if list([x[:-2],i]) in cocky:
                                cocky[cocky.index(list([x[:-2],i]))] = doc
                else:
                    if x[:-1] in labels:
                        labels.pop(labels.index(x[:-1]))
                        for i in range(0,10):
                            if list([x[:-1],i]) in cocky:
                                cocky.pop(cocky.index(list([x[:-1],i])))
                        
            #print(labels)        
            #print(cocky)
            soucet  = pocitej(cocky)
            print(soucet)
parse("input.txt")