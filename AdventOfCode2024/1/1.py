from os.path import realpath, dirname, join

def parse(s:str):
    prvni:list = []
    druhy:list = []
    soucet = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        for line in file.read().split('\n'):
            dvojice = line.split(' ')
            prvni.append(dvojice[0])
            druhy.append(dvojice[3])
    prvni.sort()
    druhy.sort()
    for i in range(0,len(prvni)):
        rozdil:int = int(prvni[i]) - int(druhy[i])
        if rozdil < 0 :
            rozdil = rozdil * -1
        soucet += rozdil
    print(prvni)
    print(druhy)
    print(soucet)


parse("input.txt")
