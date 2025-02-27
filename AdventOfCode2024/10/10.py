from os.path import realpath, dirname, join
def parse(s:str):
    mrizka = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        for r,radek_s in enumerate(file.read().split("\n")):
            radek = []
            for s,pos in enumerate(radek_s):
                radek.append(list([r,s,int(pos)]))
            mrizka.append(radek)
    print(mrizka)
    box = []
    for i in range(-1,2):
        for j in range(-1,2):
            box.append(list([i,j]))
    for b in box:
        if 0 not in b :
            box.pop(box.index(b))
    box.pop(box.index([0,0]))
    print(box)
    print("\n")
    soucet = 0
    for r in mrizka:
        for pos in r:
            if pos[2] == 0:
                moznosti = []
                x = pos[1]
                y = pos[0]
                for i,j in box:
                    if 0 <= x+i < len(r) and 0 <= y+j < len(mrizka):
                        if mrizka[y+j][x+i][2] == pos[2]+1:
                            moznosti.append(mrizka[y+j][x+i])
                done = False
                # print(moznosti)
                while done == False:
                    new_moznosti = []
                    for m in moznosti:
                        x = m[1]
                        y = m[0]
                        for i,j in box:
                            if 0 <= x+i < len(r) and 0 <= y+j < len(mrizka):
                                if mrizka[y+j][x+i][2] == m[2]+1 and mrizka[y+j][x+i] not in new_moznosti:
                                    new_moznosti.append(mrizka[y+j][x+i])
                        if new_moznosti != []:
                            moznosti = list(new_moznosti)
                        
                    # print(moznosti)
                    if moznosti[0][2] == 9:
                        print(moznosti)
                        soucet += len(moznosti)
                        done = True
    print(soucet)


                


parse("input.txt")