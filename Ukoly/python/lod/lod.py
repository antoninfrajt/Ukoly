from os.path import realpath, dirname, join
class Ship:
    __sever:int = 0
    __vychod:int =0
    __stupne:int = 90

    def __init__(self,stupne:int, sever:int, vychod:int)-> None:
        self.__sever=sever
        self.__vychod = vychod
        self.__stupne = stupne
    
    def __repr__(self) -> str:
        return f"Severni souradnice je: {self.__sever}\nVychodni souradnice je: {self.__vychod}\nDohromady to je: {abs(self.__sever)+abs(self.__vychod)}"
    
    def pohyb(self, smer:str, hodnota:int)->None:
        match smer:
            case 'L':
                hodnota = hodnota*(-1)
                self.rotace(hodnota)
            case 'R':
                self.rotace(hodnota)
            case 'N':
                self.__sever += hodnota
            case 'S':
                self.__sever -= hodnota
            case 'E':
                self.__vychod += hodnota
            case 'W':
                self.__vychod -= hodnota
            case 'F':
                match self.__stupne:
                    case 0 :
                        self.__sever += hodnota
                    case 90:
                        self.__vychod += hodnota
                    case 180:
                        self.__sever -= hodnota
                    case 270:
                        self.__vychod -= hodnota
                    case _: pass
            case _: pass

    def rotace(self, hodnota:int):
        self.__stupne += hodnota
        if self.__stupne >= 360:
            self.__stupne -= 360
        if self.__stupne < 0:
            self.__stupne += 360
    
    def naviguj(self, soubor:str):
        with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                self.pohyb(line[0],int(line[1:]))
                
def main():
    NovaLod = Ship(90,0,0)
    NovaLod.naviguj("input.txt")
    print(NovaLod)
    
# main()
if __name__ == "__main__":
    main()