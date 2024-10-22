<<<<<<< HEAD
from os.path import join,dirname,realpath
bar:dict = {"red":"1", "green":"2", "blue":"3"}
class Game:
    __num:int = 0
    __red:int = 0
    __green:int = 0
    __blue:int = 0
    def __init__(self,num:int,red:int,green:int,blue:int):
        self.__num = num
        self.__red = red
        self.__blue = blue
        self.__green = green
    def __gt__(self,other):
        if self.__red > other.__red or self.__green > other.__green or self.__blue > other.__blue:
            return True
        else:
            return False
def CreateGame(g:int,revealed:list,b:list)->Game:
    red:int = 0
    green:int = 0
    blue:int = 0
    changed:list = []
    for x in revealed:
        for e in b:
            if e in x:
                newx:str=x.replace(e,b[e])
                x = newx
        for u in x.split(','):
            changed.append(u)
    for y in changed:
        match y[-1]:
            case '1':
                if int(y[:-2]) > red:
                    red = int(y[:-2])
            case '2':
                if int(y[:-2]) > green:
                    green = int(y[:-2])
            case '3':
                if int(y[:-2]) > blue:
                    blue = int(y[:-2])
    print("red:",red,"blue:",blue,"green",green)
    return Game(g,red,green,blue)    
def Res(soubor:str,bar:dict,g:Game):
    soucet:int = 0   
    with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                print(line)
                l:list= line.split(';')
                prvni:list =l[0].split(':')
                cisloHry:str = ""
                cislo:int = 0
                hra = prvni[0]
                for x in hra:
                    #print(x)
                    if x.isnumeric() == True:
                        #print("ano")
                        cisloHry+=x
                print(cisloHry)
                cislo= int(cisloHry)
                l.pop(0)
                l.append(prvni[1])
                gameska:Game = CreateGame(cislo,l,bar)
                if gameska>g:
                    print("nemožná hra")
                else:
                    print(soucet)
                    soucet+=cislo
                    print(soucet)
    print(soucet)
mozne = Game(0,12,13,14)
Res("input.txt",bar,mozne)



=======
from os.path import join,dirname,realpath
bar:dict = {"red":"1", "green":"2", "blue":"3"}
class Game:
    __num:int = 0
    __red:int = 0
    __green:int = 0
    __blue:int = 0
    def __init__(self,num:int,red:int,green:int,blue:int):
        self.__num = num
        self.__red = red
        self.__blue = blue
        self.__green = green
    def __gt__(self,other):
        if self.__red > other.__red or self.__green > other.__green or self.__blue > other.__blue:
            return True
        else:
            return False
def CreateGame(g:int,revealed:list,b:list)->Game:
    red:int = 0
    green:int = 0
    blue:int = 0
    changed:list = []
    for x in revealed:
        for e in b:
            if e in x:
                newx:str=x.replace(e,b[e])
                x = newx
        for u in x.split(','):
            changed.append(u)
    for y in changed:
        match y[-1]:
            case '1':
                if int(y[:-2]) > red:
                    red = int(y[:-2])
            case '2':
                if int(y[:-2]) > green:
                    green = int(y[:-2])
            case '3':
                if int(y[:-2]) > blue:
                    blue = int(y[:-2])
    print("red:",red,"blue:",blue,"green",green)
    return Game(g,red,green,blue)    
def Res(soubor:str,bar:dict,g:Game):
    soucet:int = 0   
    with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                print(line)
                l:list= line.split(';')
                prvni:list =l[0].split(':')
                cisloHry:str = ""
                cislo:int = 0
                hra = prvni[0]
                for x in hra:
                    #print(x)
                    if x.isnumeric() == True:
                        #print("ano")
                        cisloHry+=x
                print(cisloHry)
                cislo= int(cisloHry)
                l.pop(0)
                l.append(prvni[1])
                gameska:Game = CreateGame(cislo,l,bar)
                if gameska>g:
                    print("nemožná hra")
                else:
                    print(soucet)
                    soucet+=cislo
                    print(soucet)
    print(soucet)
mozne = Game(0,12,13,14)
Res("input.txt",bar,mozne)



>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
