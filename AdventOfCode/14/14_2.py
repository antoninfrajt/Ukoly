from os.path import realpath, dirname, join
def cyklus(g:list)->list:
    p = len(g)
    g = naklon(g)
    g = otoc(g,p)
    p = len(g)
    g = naklon(g)
    g = otoc(g,p)
    p = len(g)
    g = naklon(g)
    g = otoc(g,p)
    p = len(g)
    g = naklon(g)
    g = otoc(g,p)
    return g


def otoc(g:list,p:int)->list:
    doc = []
    sloupec = []
    ng:list = []
    for x in g:
        for km in x:
            doc.append(list([p-1-km[1],km[0],km[2]]))
    doc.sort()
    #print(doc)
    for i in range(0,p):
        sloupec = []
        for x in doc:
            if x[0] == i:
                sloupec.append(x)
        #print(sloupec)
        ng.append(sloupec)
    return ng

        
            


def pocitej(g:list)->int:
    s:int = 0
    for x in g:
        for km in x:
            if km[2] == 'O':
                s += len(g) - km[1]
                #print(s)
        #print("sloupec" + str(km[0]+1))
        #print(s)
    return s
def naklon(g:list)->list:
    poz:int = 0
    for x in g:
        poz = 0
        for km in x:
            match km[2]:
                case 'O':
                    #print("nula")
                    idx = x.index(km)
                    #print(km)
                    #print(x)
                    x.pop(idx)
                    doc = list([km[0],poz,"O"])
                    x.append(doc)
                    x.sort()
                    #print(x)
                    poz += 1
                case '#':
                    #print("has")
                    poz = km[1] + 1
    return g


def parse(s:str):
    grid:list = []
    soucet:int = 0
    pocet:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            radek = soubor[0]
            pocet = len(soubor)
            for i in range(0,len(radek)):
                doc:list = []
                for c,line in enumerate(soubor):
                    if line[i] != ".":
                        doc.append(list([i,c,line[i]]))
                grid.append(doc)
            print("pred")
            for x in grid:
                print(x)
            for i in range(0,242):
                print(str(i+1) + ":")
                grid = cyklus(grid)
                #for nx in grid:
                    #print(nx)
            soucet = pocitej(grid)
            print(soucet)     
parse("input.txt")
cislo = 1000000000 % 22
print(cislo)