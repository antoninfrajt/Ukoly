from os.path import realpath, dirname, join
def compare(k:list,l:list):
    pocet = 0
    for lock in l:
        for key in k:
            fit = True
            for i in range(0,5):
                if lock[i] <= key[i]:
                    pass
                else:
                    fit = False
            if fit:
                pocet += 1
    print(pocet)

def hashuj(l:list):
    idxo = 0
    if l[0][0] == "#":
        for object in l:
            o_hash = [0,0,0,0,0]
            c_radku = 0
            for radek in object.split("\n"):
                idxr = 0
                for c in radek:
                    if c == "#":
                        o_hash[idxr] = c_radku
                    idxr += 1
                c_radku += 1
            l[idxo] = o_hash
            idxo += 1
        print(l)
    else:
        for object in l:
            o_hash = [0,0,0,0,0]
            c_radku = 0
            for radek in object.split("\n"):
                idxr = 0
                for c in radek:
                    if c == ".":
                        o_hash[idxr] = c_radku
                    idxr += 1
                c_radku += 1
            l[idxo] = o_hash
            idxo += 1
        print(l)
        



def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        all = file.read().split("\n\n")
        keys = []
        locks = []
        for a in all:
            if a[0] == "#":
                locks.append(a)
            else:
                keys.append(a)
        hashuj(locks)
        hashuj(keys)
        compare(keys,locks)


parse ("input.txt")