from os.path import realpath, dirname, join
    
def pocitej(r:str,c:list)->int:
    has:list = []
    pocet = r.count('?')
    print(r,pocet)

             
def parse(s:str):
    radek:str = ""
    cisla:list = []
    soucet:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for line in soubor:
                rc = line.split(' ')
                radek = rc[0]
                cisla  = rc[1].split(',')
                pocitej(radek,cisla)

parse("test.txt")