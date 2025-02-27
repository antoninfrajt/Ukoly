from os.path import realpath, dirname, join
def kontroluj(p:list,t:list):
    soucet = 0
    for tisk in t:
        ok:bool = True
        for prav in p:
            if prav[0] in tisk and prav[1] in tisk:    
                if (prav.index(prav[0]) < prav.index(prav[1]) and tisk.index(prav[0]) > tisk.index(prav[1])) or (prav.index(prav[0]) > prav.index(prav[1]) and tisk.index(prav[0]) < tisk.index(prav[1])):
                    ok = False
        if ok:
            soucet += int(tisk[int((len(tisk)-1)/2)])
            print(tisk[int((len(tisk)-1)/2)])
            print(soucet)
def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        file_s = file.read().split("\n\n")
        pravidla_s = file_s[0]
        pravidla = []
        for radek in pravidla_s.split("\n"):
            pravidla.append(radek.split("|"))
        # print(pravidla_s)
        # print(pravidla)
        print("\n")
        tisky_s = file_s[1]
        tisky = []
        for radek in tisky_s.split("\n"):
            tisky.append(radek.split(","))
        # print(tisky_s)
        # print(tisky)
        kontroluj(pravidla,tisky)


parse("test.txt")