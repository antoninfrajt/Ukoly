from os.path import realpath, dirname, join
# funkce pro hledání cesty
def find_path(m:list)->str: 
    """Funkce která najde nejkratší cestu. Vstupem je mřížka ve formátu list[list], která popisuje bludiště. Výstupem je string použitých směrů (>>^^vv<<)"""
    box = [] # souřadnice pro pohyb
    for i in range(-1,2):
        for j in range(-1,2):
            box.append(list([i,j]))
    for b in box:
        if 0 not in b :
            box.pop(box.index(b))
    box.pop(box.index([0,0]))
    bad = [] # list pro zapisování špatných odboček
    visited = [] # list navštívených křižovatek 
    done = False 
    for r in m:
        for s in r:
            if s[2] == "S": # vyhledám start dráhy
                start = s # ukládá startovní pozici
                pos = s # ukládá aktuální pozici
                pred = [] # ukládá předchozí pozici
                path = "" # zapisuje cestu
                cross = [] # ukládá list odboček na poslední křižovatce
                while pos[2] != "E" and done == False: # funkce jede dokud nejsme na konci dráhy
                    correct = [] # ukládá možné cesty z aktuální pozice
                    for b in box:
                        idx = 0
                        # najde další políčko kam se můžeme posunout 
                        if m[pos[0]+b[0]][pos[1]+b[1]][2] in list([".","E"]) and m[pos[0]+b[0]][pos[1]+b[1]] != pred and m[pos[0]+b[0]][pos[1]+b[1]] not in bad and m[pos[0]+b[0]][pos[1]+b[1]] not in visited:
                            # print(m[pos[0]+b[0]][pos[1]+b[1]])
                            correct.append(m[pos[0]+b[0]][pos[1]+b[1]])
                            next = m[pos[0]+b[0]][pos[1]+b[1]]
                    # funkce pro identifikaci slepé cesty
                    if correct == []:
                        # print("slepa")
                        # print(path)
                        visited = []
                        next = start
                        if cross[idx] not in bad:
                            bad.append(cross[idx])
                        # print(bad)
                        path = ""
                    # když najdu víc než jednu cestu vytvořím křižovatku
                    if len(correct) > 1:
                        next = correct[idx]
                        cross = list(correct)
                        visited.append(pos)
                        # print(cross)
                        idx += 1
                    # if pos == m[1][1]:
                    #     done = True
                    # zapíše krok, který provedl
                    match [next[0]-pos[0],next[1]-pos[1]]:
                        case [1,0]:
                            path += "v"
                        case [-1,0]:
                            path += "^"
                        case [0,1]:
                            path += ">"
                        case [0,-1]:
                            path += "<"
                    pred = pos # posun na další pozici
                    pos = next
                # print(len(path))
                return path

def cheat(m:list)->list: 
    """Funkce založená na find_path. Funkce prochází cestu a hledá místa, kde může cheatovat. Vstupem je mřížka ve formátu list[list], která popisuje dané bludiště. Výstupem je list délky cheatů"""
    # začátek funguje stejně jako funkce find_path
    box = [] 
    for i in range(-1,2):
        for j in range(-1,2):
            box.append(list([i,j]))
    for b in box:
        if 0 not in b :
            box.pop(box.index(b))
    box.pop(box.index([0,0]))
    print(box)
    done = False
    cheated = [] # list už použitých cheatů
    cheats = [] # výsledek funkce
    for r in m:
        for s in r:
            if s[2] == "S": 
                pos = s
                pred = []
                while pos[2] != "E" and done == False:
                    walls =[] # list všech zdí v okolí aktuální pozice
                    # print(pos)
                    # print("\n")
                    for b in box:
                        if m[pos[0]+b[0]][pos[1]+b[1]][2] in list([".","E"]) and m[pos[0]+b[0]][pos[1]+b[1]] != pred:
                            # print(m[pos[0]+b[0]][pos[1]+b[1]])
                            next = m[pos[0]+b[0]][pos[1]+b[1]]
                        elif m[pos[0]+b[0]][pos[1]+b[1]] != pred: # vyhledává zdi v okolí pozice
                            walls.append(list([m[pos[0]+b[0]][pos[1]+b[1]],b]))
                    # print(walls)
                    for wall,b in walls: 
                        if 0 <= wall[0]+b[0] < len(m) and 0 <= wall[1]+b[1] < len(r): #brání IndexError
                            if m[wall[0]+b[0]][wall[1]+b[1]][2] in list([".","E"]) and wall not in cheated: #zeď se dá cheatnout jen když se přímo za ní nachází cesta
                                print(m[wall[0]][wall[1]])
                                # print(m[next[0]][next[1]])
                                m[wall[0]][wall[1]][2] = "." # změní zeď na cestu
                                m[next[0]][next[1]][2] = "#" # změní cestu kterou by se normálně vydal na zeď
                                # m[2][3][2] = "#"
                                # print(m)
                                print(find_path(m))
                                cheats.append(len(find_path(m))) # provede hledání cesty ve změněném bludišti
                                m[wall[0]][wall[1]][2] = "#" # vrátí bludiště do původního stavu
                                m[next[0]][next[1]][2] = "."
                                # m[2][3][2] = "#"
                                cheated.append(wall) # zapíše provedený cheat do použitých cheatů
                    pred = pos # posun pozice
                    pos = next
                print(cheats)
                return cheats # vrátí list cheatů

    
def parse(s:str):
    mrizka = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file: # parsování textu na mřížku
        for r,radek_s in enumerate(file.read().split("\n")):
            radek = []
            for s,pos in enumerate(radek_s):
                radek.append(list([r,s,pos]))
            mrizka.append(radek)
    print(mrizka)
    delka = find_path(mrizka) # hledání původní cesty
    cheaty = cheat(mrizka) # hledání všech cheatů
    cheaty_best = [] # list kam program zapíše nejlepší cheaty
    for c in cheaty:
        c = len(delka) - c
        if c >= 4:
            cheaty_best.append(c)
    print(cheaty_best)
    print(len(cheaty_best)) # nakonec program vyhodí pouze počet cheatů

parse("input.txt")
