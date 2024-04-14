from os.path import realpath, dirname, join

        
def parse(s:str):
    grid:list = []
    prazdny:list = []
    min:list = []
    komb:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for r,line in enumerate(soubor):
                for s,x in enumerate(line):
                    if x == "#":
                        grid.append(list([r,s,x]))
            doc:list = []
            for x in grid:
                doc.append(x[0])
            for i in range(0,len(soubor)):
                if i in doc:
                    pass
                else:
                    if i not in prazdny:
                        prazdny.append(i)
            for r,s,x in grid:
                d = r
                for y in prazdny:
                    if d > y:
                        idx = grid.index(list([r,s,x]))
                        r += 999999
                        grid[idx] = list([r,s,x])
            doc = []
            prazdny.clear()
            for x in grid:
                doc.append(x[1])
            for i in range(0,len(line)):
                if i in doc:
                    pass
                else:
                    if i not in prazdny:
                        prazdny.append(i)
            for r,s,x in grid:
                d = s
                for y in prazdny:
                    if y < d:
                        idx = grid.index(list([r,s,x]))
                        s += 999999
                        grid[idx] = list([r,s,x])
            gala:list = enumerate(grid)
            #print(list(enumerate(grid)))
            for c,x in enumerate(grid):
                for d,p in enumerate(grid):
                    rozdil = (abs(x[0]-p[0])+abs(x[1]-p[1]))
                    if list([d,c]) not in komb and c!=d:
                        komb.append(list([c,d]))
                    if list([c,d]) in komb:
                        min.append(list([rozdil,list([c,d])]))
            min.sort()
            soucet:int = 0
            for x,y in min:
                soucet += x
            print(soucet)
parse("input.txt")