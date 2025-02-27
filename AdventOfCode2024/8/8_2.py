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
                        newxi = i[1] 
                        newxj = j[1]
                        newyi = i[0]
                        newyj = j[0]
                        x = i[1] - j[1]
                        y = i[0] - j[0]
                        while 0 <= newxi < radek and 0 <= newyi < radek:
                            if list([newyi,newxi]) not in anti:
                                anti.append(list([newyi,newxi]))
                            newxi = newxi + x
                            newyi = newyi + y
                        while 0 <= newxj < radek and 0 <= newyj < radek:
                            if list([newyj,newxj]) not in anti:
                                anti.append(list([newyj,newxj]))
                            newxj = newxj - x
                            newyj = newyj - y

                        # print(anti)
            # print(anti)
            # print("\n")
        print(len(anti))
        print(sloupec)

parse("input.txt")