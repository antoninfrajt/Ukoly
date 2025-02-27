from os.path import realpath, dirname, join

def parse(s:str):
    prvni:list = []
    druhy:list = []
    pocet = 0
    chyba = -1
    poradi = 1
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        for line in file.read().split('\n'):
            print("\n")
            print(poradi)
            savedrep = line.split(' ')           
            # print("saved")
            # print(savedrep)
            report:list = []
            for i in savedrep:
                report.append(i)
            oprava = False
            for p in range (0,4):
                if p > 0 and oprava == True:
                    # print("saved")
                    # print(savedrep)
                    report = []
                    for i in savedrep:
                        report.append(i)
                    if p == 1:
                        index = chyba -1
                    del report[index]
                    index += 1
                smer:str = ' '
                safe:bool = True
                if p == 0 or oprava:
                    print(report)
                    for i in range (0,len(report)-1):
                        # print(smer)
                        # print(report[i],report[i+1])
                        if int(report[i]) > int(report[i+1]) and (smer == "d" or smer == " " ):
                            smer = "d"
                            if int(report[i]) - int(report[i+1]) >= 4:
                                safe = False
                                chyba = i
                                oprava = True
                                print("chyba vetsi")
                                break
                        elif int(report[i]) < int(report[i+1]) and (smer == "u" or smer == " "):
                            smer = "u"
                            if int(report[i+1]) - int(report[i]) >= 4:
                                safe = False
                                chyba = i
                                oprava = True
                                print("chyba mensi")
                                break
                        else:
                            safe = False
                            chyba = i
                            oprava = True
                            print("chyba rovno")
                            break
                        if safe == False:
                            break
                    if safe:
                            oprava = False
            if safe:
                pocet += 1
                print("safe")
            else:
                print("unsafe")
            poradi += 1
    print(pocet)

parse("input.txt")