<<<<<<< HEAD
from os.path import realpath, dirname, join
def naviguj(s:list,g:list,k:list,p:list)->list:
    vys:list = []
    #print(len(s))
    if len(s) > 1:
        for x in s:
            match x[0]:
                case '.':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                    vys.append(g[idx])
                case '-':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys = g[idx]
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                        vys = g[idx]
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                case '|':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys = g[idx]
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys = g[idx]

                case '\\':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]-1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    vys = g[idx]
                case '/':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]-1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    vys = g[idx]
    else:
        match x[0]:
                case '.':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                    vys = g[idx]
                case '-':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys = g[idx]
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                        vys = g[idx]
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                case '|':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys = g[idx]
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys = g[idx]

                case '\\':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]-1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    vys = g[idx]
                case '/':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]-1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    vys = g[idx]
    return vys
def parse(s:str):
    grid:list = []
    znaky:list = []
    kord:list = []
    laser:list = []
    skupiny:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for r,line in enumerate(soubor):
                for s,x in enumerate(line):
                    if x != " ":
                        grid.append(list([x,r,s]))
                        znaky.append(x)
                        kord.append(list([r,s]))
            print(grid)

=======
from os.path import realpath, dirname, join
def naviguj(s:list,g:list,k:list,p:list)->list:
    vys:list = []
    #print(len(s))
    if len(s) > 1:
        for x in s:
            match x[0]:
                case '.':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                    vys.append(g[idx])
                case '-':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys = g[idx]
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                        vys = g[idx]
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                case '|':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys = g[idx]
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys = g[idx]

                case '\\':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]-1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    vys = g[idx]
                case '/':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]-1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    vys = g[idx]
    else:
        match x[0]:
                case '.':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                    vys = g[idx]
                case '-':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys = g[idx]
                    if s[2] < p[2]:
                        idx = k.index(list([s[1],s[2]-1]))
                        vys = g[idx]
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1],s[2]-1]))
                        vys.append(g[idx])
                case '|':
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys.append(g[idx])
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys.append(g[idx])
                    if s[1] < p[1]:
                        idx = k.index(list([s[1]-1,s[2]]))
                        vys = g[idx]
                    if s[1] > p[1]:
                        idx = k.index(list([s[1]+1,s[2]]))
                        vys = g[idx]

                case '\\':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]-1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]+1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    vys = g[idx]
                case '/':
                    if s[1] < p[1]:
                        idx = k.index(list([s[1],s[2]+1])) 
                    if s[1] > p[1]:
                        idx = k.index(list([s[1],s[2]-1]))
                    if s[2] > p[2]:
                        idx = k.index(list([s[1]-1,s[2]]))
                    if s[2] < p[2]:
                        idx = k.index(list([s[1]+1,s[2]]))
                    vys = g[idx]
    return vys
def parse(s:str):
    grid:list = []
    znaky:list = []
    kord:list = []
    laser:list = []
    skupiny:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for r,line in enumerate(soubor):
                for s,x in enumerate(line):
                    if x != " ":
                        grid.append(list([x,r,s]))
                        znaky.append(x)
                        kord.append(list([r,s]))
            print(grid)

>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
parse("test.txt")