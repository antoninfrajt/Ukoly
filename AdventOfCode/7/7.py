from os.path import realpath, dirname, join
jedna:list = []
dva:list = []
dvadva:list = []
tri:list = []
dvatri:list = []
ctyri:list = []
pet:list = []
kar:dict  = {
        "2":0,
        "3":1,
        "4":2,
        "5":3,
        "6":4,
        "7":5,
        "8":6,
        "9":7,
        "T":8,
        "J":9,
        "Q":10,
        "K":11, 
        "A":12
    }
def porovnej(a:str,b:str)->str:
    kar:dict  = {
        "2":0,
        "3":1,
        "4":2,
        "5":3,
        "6":4,
        "7":5,
        "8":6,
        "9":7,
        "T":8,
        "J":9,
        "Q":10,
        "K":11, 
        "A":12
    }
    for i in range(0, len(a)):
        if kar[a[i]] > kar[b[i]]:
            return a
        if kar[b[i]] > kar[a[i]]:
            return b
def urci(txt:str)->int:
    score:int = 0
    for k in kar.keys():
        #print(txt.count(k))
        if txt.count(k) == 5:
            score += 6
            pet.append(txt)
        if txt.count(k) == 4:
            score += 5
            ctyri.append(txt)
        if txt.count(k) == 3:
            score += 3
        if txt.count(k) == 2:
            score += 1
    if score == 4:
        dvatri.append(txt)
    if score == 2:
        dvadva.append(txt)
    if score == 3:
        tri.append(txt)
    if score == 1:
        dva.append(txt)
    if score == 0:
        jedna.append(txt)
    return score
            
def parse(s:str):
    karty:dict = []
    sazky:list = []
    celkem:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for x in soubor:
                x.strip()
                karty.append(x.split(' ')[0])
                sazky.append(int(x.split(' ')[1]))
            #print(karty)
            for i in range(0,1):
                for x in karty:
                    #print(x)
                    idx = karty.index(x)
                    if (idx+1) >= len(karty):
                        idx = karty.index(x)-1 
                    a = urci(karty[idx])*2
                    b = urci (karty[idx+1])*2
                    if a == b:
                        #print(porovnej(karty[idx],karty[idx+1]))
                        if karty[idx] == porovnej(karty[idx],karty[idx+1]):
                            a += 1
                        else:
                            b += 1
                    if a > b:
                        #print(a,b)
                        doc:str = karty[idx]
                        karty[idx] = karty[idx+1]
                        karty[idx+1] = doc
                        doc2:int = sazky[idx]
                        sazky[idx] = sazky[idx+1]
                        sazky[idx+1] = doc2
            print(karty)
                #print(sazky)
            for x in sazky:
                #print(str(x)+"*"+str(sazky.index(x)+1))
                celkem += x*(sazky.index(x)+1)
            print(celkem)
parse("input.txt")
jedna.sort(key = porovnej(a,b))
dva.sort()
dvadva.sort()
dvatri.sort()
tri.sort()
ctyri.sort()
pet.sort()
print(jedna,dva,dvadva,tri,dvatri,ctyri,pet)
