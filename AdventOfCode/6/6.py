from os.path import realpath, dirname, join
def zavod(c:int,v:int)->int:
    pocet:int = 0
    mv:int = 0
    for i in range(0,c+1):
        mv = i*(c-i)
        if mv > v:
             pocet += 1
    return pocet
def parse(s:str):
    cislo:list =[]
    vzd:str = ""
    cas:str = ""
    pocet:int = 1 
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for x in soubor[0][6:].split(' '):
                x.strip()
                if x != "":
                    cislo.append(x)
            print(cislo)
            cas = cas.join(cislo)
            print(cas)
            cislo.clear()
            for x in soubor[1][9:].split(' '):
                x.strip()
                if x != "":
                    cislo.append(x)
            vzd  = vzd.join(cislo)
            print(vzd)
            print(cas)
            cas.strip()
            vzd.strip()
            pocet = zavod(int(cas),int(vzd))
            print(pocet)
            

parse("input.txt")