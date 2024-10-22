from os.path import realpath, dirname, join
def NapisZadani(o:list)->dict:
    zad:dict = {}
    PrvRad:str = o[0]
    txt = PrvRad.replace(" ","")
    o.pop(0)
    pr:list = []
    for x in txt:
        idx = PrvRad.find(x)
        h:list = []
        for y in o:
            if y[idx] == " ":
                pass
            else:
                h.append(y[idx])
        zad[x] = h
    return zad
def pohyb(kolik:int,odkud:str, kam:str, hr:dict)->dict:
    presun:list = []
    for i in range(0,kolik):
        hr[kam].append(hr[odkud][-1])
        hr[odkud].pop(-1)
    return hr


    
def parse(s:str):
    obs:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n\n')
            print(soubor[0])
            for line in soubor[0].split('\n'):
                obs.append(line)
            obs.reverse()
            print(obs)
            hromadky:dict = NapisZadani(obs)
            print(hromadky)
            print(",")
            for line in soubor[1].split('\n'):
                print(line)
                udaje:list = []
                for x in line.split(' '):
                    if x.isdigit() == True:
                        udaje.append(x)
                kolik:int = int(udaje[0])
                odkud:str = udaje[1]
                kam:str = udaje[2]
                print("pohyb")
                hromadky = pohyb(kolik,odkud,kam,hromadky)
                print(hromadky)
                udaje = []
            nahore:str = ""
            for x in range(1,int(len(hromadky)+1)):
                if hromadky[str(x)] == []:
                    pass
                else:
                    nahore+=str(hromadky[str(x)].pop(-1))
    print(nahore)

j:list = [" 1   2   3 ","[Z] [M] [P]","[N] [C]    ","    [D]    "]
#NapisZadani(j)
line:str = "[W] [P] [P] [D] [G] [P] [B] [P] [V]" 
l:int = line.find("")
parse("input.txt")
g:dict = {}
for i in range(1,10):
    h:list = []
    for j in range(1,10):
        h.append(j)
    g[i] = h
#print(g)

               