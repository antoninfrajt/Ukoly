from os.path import realpath, dirname, join

def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        typy =[]
        seznam = {}
        radek = 0
        for r,line in enumerate(file.read().split("\n")):
            radek += 1
            sloupec = 0
            for s,z in enumerate(line):
                sloupec += 1
                if z != ".":
                    if z not in typy:
                        typy.append(z)
                        seznam[z] = []
                    if list([r,s]) not in seznam[z]:
                        seznam[z].append(list([r,s]))
        print(typy)
        print(seznam)
        anti = []
        for l in seznam.values():
            for i in l:
                for j in l:
                    if i != j:
                        # print(i,j)
                        x = i[1] - j[1]
                        y = i[0] - j[0]
                        # print(y,x)
                        if 0 <= i[0]+y < radek and 0 <= i[1]+x < radek:
                            if list([i[0]+y,i[1]+x]) not in anti:
                                anti.append(list([i[0]+y,i[1]+x]))
                        if 0 <= j[0]-y < radek and 0 <= j[1]-x < radek:
                            if list([j[0]-y,j[1]-x]) not in anti:
                                anti.append(list([j[0]-y,j[1]-x]))
                        # print(anti)
            print(anti)
            print("\n")
        print(len(anti))
        print(sloupec)

parse("input.txt")