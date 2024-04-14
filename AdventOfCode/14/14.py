from os.path import realpath, dirname, join
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
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            radek = soubor[0]
            for i in range(0,len(radek)):
                doc:list = []
                for c,line in enumerate(soubor):
                    if line[i] != ".":
                        doc.append(list([i,c,line[i]]))
                grid.append(doc)
            #print("pred")
            #for x in grid:
                #print(x)
            grid = naklon(grid)
            #print("po")
            #for nx in grid:
                #print(nx)
            soucet = pocitej(grid)
            print(soucet)      
parse("input.txt")