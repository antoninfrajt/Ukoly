from os.path import realpath, dirname, join
def NaString(l:list)->str:
    string:str = ","
    for i in range(int(l[0]),int(l[1])+1):
        string += str(i)+","
    return string
def Obsahuje(prv:str,dru:str)->bool:
    obs:bool = False
    if prv in dru or dru in prv:
        obs= True
    return obs         
def parse(s:str):
    ano:int = 0
    ne:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                dvoj:list = line.split(',')
                print(dvoj)
                prv:str = ""
                dru:str = ""
                prv:str = NaString(dvoj[0].split('-'))
                dru:str = NaString(dvoj[1].split('-'))
                obs:bool = Obsahuje(prv,dru)
                print(prv+"\n"+dru)
                if obs == True:
                    print("ano")
                    ano += 1
                else:
                    print("ne")
                    ne += 1
    print("Ano:"+str(ano)+"Ne:"+str(ne))
parse("input.txt")


