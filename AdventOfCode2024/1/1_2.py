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
    for i in range(0,len(prvni)):
        pocet:int = 0
        for j in range (0,len(druhy)):
            if prvni[i] == druhy[j]:
                pocet += 1
        rozdil = int(prvni[i]) * pocet               
        soucet += rozdil
    print(prvni)
    print(druhy)
    print(soucet)


parse("input.txt")