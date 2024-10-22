from os.path import realpath, dirname, join
def hash (s:str)->int:
    kod:int = 0
    for x in s:
        kod += ord(x)
        kod = kod*17
        kod = kod % 256
    return kod
def parse(s:str):
    soucet:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split(',')
            for x in soubor:
                print(x)
                soucet += hash(x)
            print(soucet)
parse("input.txt")
#hash("HASH")
