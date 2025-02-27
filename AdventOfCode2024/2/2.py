from os.path import realpath, dirname, join

def parse(s:str):
    prvni:list = []
    druhy:list = []
    pocet = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        for line in file.read().split('\n'):
            report = line.split(' ')
            smer:str = ' '
            safe:bool = True
            print(report)
            for i in range (0,len(report)-1):
                print(smer)
                print(report[i],report[i+1])
                if int(report[i]) > int(report[i+1]) and (smer == "d" or smer == " " ):
                    smer = "d"
                    if int(report[i]) - int(report[i+1]) >= 4:
                        safe = False
                        print("chyba vetsi")
                elif int(report[i]) < int(report[i+1]) and (smer == "u" or smer == " "):
                    smer = "u"
                    if int(report[i+1]) - int(report[i]) >= 4:
                        safe = False
                        print("chyba mensi")
                else:
                    safe = False
                    print("chyba rovno")
            if safe:
                pocet += 1
                print("safe")
            else:
                print("unsafe")
    print(pocet)

parse("input.txt")
