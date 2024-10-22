from os.path import realpath, dirname, join
def hor(g:list)->int:
    vys:int = 0
    ref:bool == False
    for i in range(1,len(g)):
        if g[i-1][1] == g[i][1]:
            #print("zacinam")
            ref = True
            #print(i)
            y = len(g)-i
            r = i
            if i > y:
                r = y
            for j in range(0,r):
                #print(g[i-j],g[i+j])
                if g[i-j-1][1] != g[i+j][1]:
                    #print(g[i-j-1],g[i+j])
                    #print("ne")
                    ref = False
            if ref == True:
                #print("ano")       
                vys = i
    #print("vys")
    print(vys)
    return vys*100
def parse(s:str):
    gridh:list = []
    gridv:list = []
    soucet:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n\n')
            for c,obraz in enumerate(soubor):
                print(str(c+1)+".")
                for x,line in enumerate(obraz.split('\n')):
                    doc:list = []
                    for y,z in enumerate(line):
                        doc.append(list([y,z]))
                    gridh.append(list([x,doc]))
                h = hor(gridh)
                #print("soucet")
                #print(soucet)
                gridh.clear()
                for s in range(0,len(obraz.split('\n')[0])):
                    doc:list = []
                    for r,line in enumerate(obraz.split('\n')):
                        doc.append(list([r,line[s]]))
                    gridv.append(list([s,doc]))
                v = hor(gridv)/100
                gridv.clear()
                #print(soucet)
                if h>v:
                    soucet += h
                else:
                    soucet += v
            print(soucet)
                        
                        
parse("input.txt")

