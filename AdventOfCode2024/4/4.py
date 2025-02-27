from os.path import realpath, dirname, join

def pozice(rd:int,sl:int,d:int,l:list)->str:
    idx = rd*d + sl
    return l[idx]

def search(l:list,s:str,d:int,v:int)->int:
    # print(d)
    pocet = 0
    idx = 0
    box:list = []
    for i in range(-1,2):
        for j in range(-1,2):
            box.append(list([i,j]))
    box.remove([0,0])
    # print(box)
    for rd,sl,n in l:
        idx = 0
        if n == s[idx]:
            # print(rd,sl)
            for x,y in box:
                idx = 1
                x += rd
                y += sl
                if v >  x >=0 and d > y >=0:
                    pismeno = pozice(x,y,d,l)
                    # print(x,y)
                    # print(pismeno)
                    if pismeno[2] == s[idx]:
                        idx += 1
                        x = x-rd
                        y = y-sl
                        # print(x,y)
                        # print(pismeno[2])
                        while idx <= len(s)-1:
                            rd += x*idx
                            sl += y*idx
                            if v >  rd >=0 and d > sl >=0:
                                pismeno = pozice(rd,sl,d,l)
                            rd = rd-x*idx
                            sl = sl - y*idx
                            if pismeno[2] == s[idx]:
                                # print(pismeno)
                                idx += 1
                                if idx == len(s):
                                    pocet += 1
                                    print(rd,sl)
                                    print(rd+x*(idx-1),sl+y*(idx-1))
                                    print(pocet)
                                    print(" ")

                            else:
                                # print(pismeno)
                                # print("ne")
                                break
            print("\n")
    print(pocet)
    print(d, v)
            



def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        radky = file.read().split("\n")
        mrizka:list = []
        slovo = "XMAS"
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
        search(index,slovo,delka,vyska)
        

            


parse ("input.txt")