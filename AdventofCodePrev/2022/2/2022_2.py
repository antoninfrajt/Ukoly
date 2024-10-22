from os.path import realpath, dirname, join
def hra(y:str,o:str)->int:
    score:int = 0
    volba:int = 0
    match y:
        case 'X':
            volba = 1
            match o:
                case 'C':
                    score += volba + 6
                case 'A':
                    score += volba + 3
                case 'B':
                    score += volba + 0
        case 'Y':
            volba = 2
            match o:
                case 'A':
                    score += volba + 6
                case 'B':
                    score += volba + 3
                case 'C':
                    score += volba + 0
        case 'Z':
            volba = 3
            match o:
                case 'B':
                    score += volba + 6
                case 'C':
                    score += volba + 3
                case 'A':
                    score += volba + 0
    return score                 
def pis(s:str):
    score:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                you:str = ""
                opponent:str = ""
                opponent = line[0]
                you = line[2]
                score += int(hra(you,opponent))
                print(score)
pis("input.txt")