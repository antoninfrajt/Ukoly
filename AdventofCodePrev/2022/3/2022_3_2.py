from os.path import realpath, dirname, join
def najdi(b:list)->int:
    item:str = ""
    value:int = 0
    for x in b[0]:
        if x in b[1] and x in b[2]:
            item = x
    if ord(item) >= 91:
        value = ord(item)-96
    else:
        value = ord(item)-38
    return value
def pis(s:str):
    valueInt:int = 0
    pocet:int= 0
    skupina:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                pocet += 1
                skupina.append(line)
                if pocet%3 == 0 :
                    value:str = najdi(skupina)
                    print(value)
                    valueInt += int(value)
                    skupina = []
    print(valueInt)
pis("input.txt")