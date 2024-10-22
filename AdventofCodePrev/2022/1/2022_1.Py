from os.path import realpath, dirname, join
elf:int = 0
def pis(s:str)->str:
    e1:list = []
    calorie:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                if len(line) != 0:
                    print (line)
                    calorie += int(line)
                    print(calorie)
                else:
                    if calorie in e1:
                         print("mame")
                    else:
                        e1.append(calorie)
                        calorie = 0
    e1.sort(reverse=True)
    print(e1[0])
    print(e1[1])                  
    print(e1[2])
    print(e1[0]+e1[1]+e1[2])               
pis("input.txt")