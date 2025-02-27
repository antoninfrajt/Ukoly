from os.path import realpath, dirname, join
def jeloop(s:list)->bool:
    if len(s) == 3:
        if s[0] == s [2]:
            return True
        else:
            s.pop(0)
            return False
    else:
        return False


def navigate(m:list):
    guard = ["^",">","<","v"]
    out = False
    loop = False
    vzdalenost = 0
    smycka = []
    zataras = []
    while out == False :
        for r in m:
            for l in r:
                if l[2] in guard:
                    # print(str(l[0]) + " " + str(l[1]))
                    match l[2]:
                        case '^':
                            if l[0]-1 >= 0:
                                if m[l[0]-1][l[1]][2] != "#":
                                    l[2] = "X"
                                    vzdalenost +=1
                                    m[l[0]-1][l[1]][2] = "^"
                                else:
                                    l[2] = ">"
                                    smycka.append(vzdalenost)
                                    vzdalenost = 0
                                    print(str(l[0]) + " " + str(l[1]))
                                    print(smycka)
                                    loop = jeloop(smycka)
                                    if loop:
                                        print("ano")
                                        pos = m[l[0]][l[1]+smycka[1]]
                                        if pos not in zataras:
                                            zataras.append(pos)
                                            loop = False
                                            smycka.pop(0)
                            else:
                                l[2] = "X"
                                out = True
                                break
                        case '>':
                            if l[1]+1 <= len(m[0])-1:
                                if m[l[0]][l[1]+1][2] != "#":
                                    l[2] = "X"
                                    vzdalenost +=1
                                    m[l[0]][l[1]+1][2] = ">"
                                else:
                                    l[2] = "v"
                                    smycka.append(vzdalenost)
                                    vzdalenost = 0
                                    print(str(l[0]) + " " + str(l[1]))
                                    print(smycka)
                                    loop = jeloop(smycka)
                                    if loop:
                                        print("ano")
                                        pos = m[l[0]+smycka[1]][l[1]]
                                        if pos not in zataras:
                                            zataras.append(pos)
                                            loop = False
                                            smycka.pop(0)
                            else:
                                l[2] = "X"
                                out = True
                                break
                        case 'v':
                            if l[0]+1 <= len(m)-1:
                                if m[l[0]+1][l[1]][2] != "#":
                                    l[2] = "X"
                                    vzdalenost +=1
                                    m[l[0]+1][l[1]][2] = "v"
                                else:
                                    l[2] = "<"
                                    smycka.append(vzdalenost)
                                    vzdalenost = 0
                                    print(str(l[0]) + " " + str(l[1]))
                                    print(smycka)
                                    loop = jeloop(smycka)
                                    if loop:
                                        print("ano")
                                        pos = m[l[0]][l[1]-smycka[1]]
                                        if pos not in zataras:
                                            zataras.append(pos)
                                            loop = False
                                            smycka.pop(0)
                            else:
                                l[2] = "X"
                                out = True
                                break
                        case '<':
                            if l[1]-1 >= 0:
                                if m[l[0]][l[1]-1][2] != "#":
                                    l[2] = "X"
                                    vzdalenost +=1
                                    m[l[0]][l[1]-1][2] = "<"
                                else:
                                    l[2] = "^"
                                    smycka.append(vzdalenost)
                                    vzdalenost = 0
                                    print(str(l[0]) + " " + str(l[1]))
                                    print(smycka)
                                    loop = jeloop(smycka)
                                    if loop:
                                        print("ano")
                                        pos = m[l[0]-smycka[1]][l[1]]
                                        if pos not in zataras:
                                            zataras.append(pos)
                                            loop = False
                                            smycka.pop(0)
                            else:
                                l[2] = "X"
                                out = True
                                break
                        
                            
    # print(m)
    pocet = 0
    for r in m:
        r_s = ""
        for l in r:
            r_s += l[2]
            if l[2] == "X":
                pocet += 1
        # print(r_s)
    print(zataras)
    
def parse(s:str):
    mrizka = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        for r,radek_s in enumerate(file.read().split("\n")):
            radek = []
            for s,pos in enumerate(radek_s):
                radek.append(list([r,s,pos]))
            mrizka.append(radek)
    print(mrizka)
    navigate(mrizka)
parse("test.txt")