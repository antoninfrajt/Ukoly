from os.path import realpath, dirname, join
def naviguj(s:list,g:list,k:list,p:list)->list:
    vys:list = []
    #print(len(s))
    znak = s[0]
    match znak:
        case '|':
            if s[1] < p[1]:
                idx = k.index(list([s[1]-1,s[2]]))
            else:
                idx = k.index(list([s[1]+1,s[2]]))
            vys = g[idx]
        case '-':
            if s[2] < p[2]:
                idx = k.index(list([s[1],s[2]-1]))
            else:
                idx = k.index(list([s[1],s[2]+1]))
            vys = g[idx]
        case 'L':
            if s[2] < p[2]:
                idx = k.index(list([s[1]-1,s[2]]))
            else:
                idx = k.index(list([s[1],s[2]+1]))
            vys = g[idx]
        case 'J':
            if s[2] > p[2]:
                idx = k.index(list([s[1]-1,s[2]]))
            else:
                idx = k.index(list([s[1],s[2]-1]))
            vys = g[idx]
        case '7':
            if s[2] > p[2]:
                idx = k.index(list([s[1]+1,s[2]]))
            else:
                idx = k.index(list([s[1],s[2]-1]))
            vys = g[idx]
        case 'F':
            if s[2] < p[2]:
                idx = k.index(list([s[1]+1,s[2]]))
            else:
                idx = k.index(list([s[1],s[2]+1]))
            vys = g[idx]
        case '.':
            vys = []
    return vys
def parse(s:str):
    grid:list = []
    znaky:list = []
    kord:list = []
    startovni:list = []
    skupiny:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for r,line in enumerate(soubor):
                for s,x in enumerate(line):
                    if x != " ":
                        grid.append(list([x,r,s]))
                        znaky.append(x)
                        kord.append(list([r,s]))
            #print(grid)
            start = grid[znaky.index("S")]
            print(start)
            if start[1] > 0:
                idx = kord.index(list([start[1]-1,start[2]]))
                if grid[idx][0] == "|" or "7" or "F":
                    startovni.append(grid[idx])
            if start[1] < len(soubor):
                idx = kord.index(list([start[1]+1,start[2]]))
                if grid[idx][0] == "|" or "J" or "L":
                    startovni.append(grid[idx])
            if start[2] > 0:
                idx = kord.index(list([start[1],start[2]-1]))
                if grid[idx][0] == "-" or "F" or "L":
                    startovni.append(grid[idx])
            if start[2] < len(line):
                idx = kord.index(list([start[1],start[2]+1]))
                if grid[idx][0] == "-" or "J" or "7":
                    startovni.append(grid[idx])
            pre = start
            print(startovni)
            for x in startovni:
                znak = x[0]
                #print(znak)
                l:list = []
                while znak != "S":
                    if x == []:
                        break
                    doc = naviguj(x,grid,kord,pre)
                    l.append(x)
                    pre = x
                    x = doc
                #print(l)
                skupiny.append(l)
            for x in skupiny:
                print(int(len(x)/2))
parse("input.txt")