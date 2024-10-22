from os.path import realpath, dirname, join
def konec(d:list)->bool:
    vys  = True
    for x in d:
        if x != 0:
            vys =  False
    return vys
def predpovez(l:list)->list:
    ll:list = []
    ll.append(l)
    doc = l
    while konec(doc) == False:
        l = doc
        doc = []
        for i in range(0,len(l)-1):
            doc.append(l[i+1]-l[i])
        ll.append(doc)
    ll.reverse()
    for i in range(0,len(ll)-1):
        ll[i+1].reverse()
        ll[i+1].append(ll[i+1][-1]-ll[i][0])
        ll[i+1].reverse()
    #for x in ll:
        #print(x)
    return ll[-1]
        
        
def parse(s:str):
    data:list = []
    soucet:int = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            for line in soubor:
                data = []
                for x in line.split(' '):
                    data.append(int(x))
                #print(data)
                data = predpovez(data)
                soucet += data[0]
            print(soucet)
parse("input.txt")