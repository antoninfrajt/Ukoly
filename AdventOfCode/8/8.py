from os.path import realpath, dirname, join
zastavky:list = []
class Stop:
    __left:str = ""
    __right:str = ""
    __name:str = ""

    def __init__(self, name:str, left:str, right:str)-> None:
        self.__name = name
        self.__left = left
        self.__right = right
    
    def pohyb(pokyn:str,name:str)->str:
        vys:str = ""
        for x in zastavky:
            if name  == x.__name:
                match pokyn:
                    case 'L':
                        vys = x.__left
                    case 'R':
                        vys = x.__right
        return vys

def parse(s:str):
    name:str = ""
    left:str = ""
    right:str = ""
    pokyny:str = ""
    pocet:int = 0
    pocty:list = []
    azastavky:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n\n')
            pokyny = soubor[0]
            aktzas = "A"
            for x in soubor[1].split("\n"):
                radek:list = x.split(" ")
                name = radek[0]
                left = radek[2][1:-1]
                right = radek[3][0:-1]
                zastavky.append(Stop(name,left,right))
            print(aktzas)
            zas = "PSA"
            cil = "Z"
            while zas[-1] != cil:
                for x in pokyny:
                    zas = Stop.pohyb(x,zas)
                    pocet += 1
                    #print(x,y)
                    if zas[-1] == cil:
                        pocty.append(pocet)
                        break
            #print(azastavky)
            print(pocty)
            print(zas)
            print()
parse("input.txt")               