from os.path import realpath, dirname, join
cord:list = []
num:list = []
pis:dict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
def SlovaNaCisla(l:str,d:dict)->str:
    l2:str = ""
    pr:bool = False
    pos:bool = False
    while pr == False:
        for x in l:
            l2 +=x
            for p in d:
                if p in l2:
                    #print("nasel")
                    newl:str=l2.replace(p,d[p])
                    l2 = newl
                    pr = True
                    break
                if pr == True:
                    break
        break
    l=l2
    print(l)
    return l
def SlovaNaCislaNaopak(l:str,d:dict)->str:
    l2:str = ""
    pos:bool = False
    while pos == False:
        for x in l:
            l2  = x+l2
            for p in d:
                if p in l2:
                    #print("nasel")
                    newl:str=l2.replace(p,d[p])
                    l2 = newl
                    pos = True
                    break
                if pos == True:
                    break
        break
    l=l2
    print(l)
    return l
def desifruj(soubor:str,l:list,n:list,pis:list):
    soucet = 0
    kod:str = ""
    prvni:bool = False
    posledni:bool = False
    for u in range(0,10):
        n.append(str(u))
    with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                chline:str=""
                print(line)
                chline = str(SlovaNaCisla(line,pis))
                for x in chline:
                    l.append(str(x))
                #print(l)
                #print(n)
                for x in l:
                    #print(x)
                    while prvni == False:
                        for i in n:
                            if x == i:
                                kod+=str(x)
                                prvni = True
                                print("ano")
                                print(x)
                                break
                        break
                    #else:
                        print("ne")
                prvni = False
                l.clear()
                line = line[::-1]
                chline=str(SlovaNaCislaNaopak(line,pis))
                for y in chline:
                    l.append(str(y))
                l.reverse()
                #print(l)
                for y in l:
                    #print(y)
                    while posledni == False:
                        for i in n:
                            if y == i:
                                kod+=str(y)
                                posledni = True
                                print("ano")
                                print(y)
                                break
                        break
                    #else:
                        print("ne")
                posledni = False
                print(kod)
                soucet+=int(kod)
                print(soucet)
                l.clear()
                kod = ""
    print(soucet)
            

desifruj("test.txt",cord,num,pis)
print(num)
#print(pis)
line:str = "eightwothree"
#SlovaNaCisla(line,pis)


