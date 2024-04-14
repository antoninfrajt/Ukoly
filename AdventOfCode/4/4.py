from os.path import realpath, dirname, join
def boduj(v:list,a:list)->int:
    score:int = 0 
    pocet:int = 0
    for ac in a:
        if ac in v and ac != "":
            pocet += 1
    if pocet != -1:
        score = 2**pocet
    return pocet
def zisk(s:int,k:dict,h:int)->dict:
    for i in range(1,s+1):
        dh:int = 0
        dh = int(h)+i
        k[dh] =k[dh]+k[h]
    return k
    

def parse(s:str):
    vyh:list = []
    akt:list = []
    HaC:list = []
    proVyh:list = []
    score:int = 0
    soucet:int = 0
    karty:dict = {}
    for i in range(1,195):
        karty[i] = 1
    hra:str = ""
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for line in soubor:
                HaC = line.split(':')
                hra = HaC.pop(0)[5:]
                print("cislo hry:" +hra)
                proVyh = HaC.pop(0).split('|')
                for Vcislo in proVyh.pop(0).strip().split(' '):
                    if Vcislo != " ":
                        vyh.append(Vcislo)
                print("vyherni")
                print(vyh)
                for Acislo in proVyh.pop(0).strip().split(' '):
                    if Acislo != " ":
                        akt.append(Acislo)
                print("aktualni")
                print(akt)
                score = boduj(vyh,akt)
                print("score:"+str(score))
                if score != 0:
                    zisk(score,karty,int(hra))
                print(hra)
                score = 0
                vyh.clear()
                akt.clear()
            soucet = sum(karty.values())
            print("soucet je:"+str(soucet))
parse("input.txt")
karty:dict = {}
for i in range(1,7):
    karty[i] = 1
print(karty)
zisk(3,karty,1)
print(karty)
zisk(2,karty,2)
print(karty)