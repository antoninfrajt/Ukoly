from os.path import realpath, dirname, join
def najdi(prv:str,dru:str)->int:
    item:str = ""
    value:int = 0
    for x in prv:
        if x in dru:
            item = x
    if ord(item) >= 91:
        value = ord(item)-96
    else:
        value = ord(item)-38
    return value
def pis(s:str):
    valueInt:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                prv:str = line[0:int(len(line)/2)]
                dru:str = line[int(len(line)/2):]
                value:str = najdi(prv,dru)
                print(value)
                valueInt += int(value)
    print(valueInt)
line:str = "vJrwpWtwJgWrhcsFMMfFFhFp"
prv:str = line[0:int(len(line)/2)]
dru:str = line[int(len(line)/2):]
value:str = najdi(prv,dru)
print(value)
pis("input.txt")
