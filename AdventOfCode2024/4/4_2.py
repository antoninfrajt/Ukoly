from os.path import realpath, dirname, join

def pozice(rd:int,sl:int,d:int,l:list)->str:
    idx = rd*d + sl
    return l[idx]

def search(l:list,d:int,v:int)->int:
    # print(d)
    pocet = 0
    box:list = []
    for i in range(-1,2,2):
        for j in range(-1,2,2):
            box.append(list([i,j]))
    print(box)
    for rd,sl,n in l:
        if n == "A":
            cross:list=[]
            for x,y in box:
                x += rd
                y += sl
                if v >  x >=0 and d > y >=0:
                    pismeno = pozice(x,y,d,l)
                    cross.append(pismeno)
                    # print(x,y)
                    # print(pismeno)
            if len(cross) == 4:
                print(rd,sl)
                print(cross)
                print(len(cross))
                scross:str = ""
                posible:list = ["SMSM","MSMS","SSMM","MMSS"]
                for j in range(0,4):
                    scross += cross[j][2]
                print (scross)
                if scross in posible:
                    pocet += 1
                    print(pocet)
                else:
                    print("ne")
            else:
                print("ne")
                    
            print("\n")
    print(box)
    print(pocet)
    print(d, v)
            



def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        radky = file.read().split("\n")
        mrizka:list = []
        vyska = 0
        index:list = []
        for n in radky:
            vyska += 1
            delka = len(n)
            radek:list = []
            for i in range (0,len(n)):
                radek.append(n[i])
            mrizka.append(radek)
        for rd,rdek in enumerate(mrizka):
            for sl,p in enumerate(rdek):
                index.append(list([rd,sl,p]))
        search(index,delka,vyska)
        

            


parse ("input.txt")