from os.path import realpath, dirname, join
import re
def rozsekni(l:list,h:int)->list:
    d:list = []
    prvni:list = list([l[0],int(h)-1])
    druhy:list = list([int(h),l[1]])
    d = list([prvni,druhy])
    return d
def uprav(s:list,c:list)->list:
    sd:list = []
    mame:list = []
    for x in s:
            l = list(x)
            mame.append(l)
            sd.append(l)
    print("sd:")
    print(sd)
    for do,z,d in c:
        d = int(d)-1
        for x in s:
            z = 80
            if z in range(int(x[0]),int(x[1])):
                k:list =rozsekni(x,z)
                print("pridavam")
                print(k)
                print(sd)
                idx = sd.index(x)
                sd.pop(idx)
                sd.extend(k)
                print(sd)
        for za,ko in s:
            if za in range(int(z),int(z)+int(d)+1) and ko in range(int(z),int(z)+int(d)+1):
                print("oba")
                print(z,str(int(z)+int(d)))
                print(str(za)+"-"+str(ko)+":"+str(int(do)-int(z)))
                idx = s.index(list([za,ko]))
                za += int(do)-int(z)
                ko += int(do)-int(z)
                doc = list([int(za),int(ko)])
                print(doc)
                mame[idx] = doc
                #print(str(x)+"+"+str(int(do)-int(z))+"="+str(mame[idx])+" in "+str(z)+"-"+str(int(z)+int(d)))
            else:
                if za in range(int(z),int(z)+int(d)+1):
                    print("jen za")
                    print(z,str(int(z)+int(d)))
                    print(str(int(z)+int(d)+1)+"-"+str(ko)+" zustava:")
                    print(str(za)+"-"+str(int(d)+int(z))+":"+str(int(do)-int(z)))
                    idx = s.index(list([za,ko]))
                    za += int(do)-int(z)
                    docza = list([int(z)+int(d)+1,ko])
                    mame[idx] = list([int(za),int(d)+int(do)])
                    print(mame[idx])
                    print(docza)
                    mame.append(docza)
                else:
                    if ko in range(int(z),int(z)+int(d)+1):
                        print("jen ko")
                        print(z,str(int(z)+int(d)))
                        print(str(za)+"-"+str(int(z)-1)+" zustava:")
                        print(str(z)+"-"+str(ko)+":"+str(int(do)-int(z)))
                        idx = s.index(list([za,ko]))
                        ko += int(do)-int(z)
                        docko = list([za,int(z)-1])
                        mame[idx] = list([int(do),int(ko)])
                        print(mame[idx])
                        print(docko)
                        if list([z,ko]) in mame:
                            mame[mame.index(list([za,ko]))] = docko
                        else:
                            mame.append(docko)
                    else:
                        if int(z) and int(z)+int(d) in range(za,ko):
                            print("jen cast")
                            print(z,str(int(z)+int(d)))
                            print(str(z)+"-"+str(int(z)+int(d))+":"+str(int(do)-int(z)))
                            idx = s.index(list([za,ko]))
                            mame[idx] = list([int(do),int(do)+int(d)])
                            doc1 = list([za,int(z)])
                            mame.append(doc1)
                            print(doc1)
                            doc2 = list([int(z)+int(d),int(ko)])
                            print(doc2)
                            mame.append(doc2)
        print(mame)
    return mame



      
def parse(s:str):
    sem:list =[]
    cis:list =[]
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n\n')
            sem2 = soubor[0][7:].split(' ')
            for i in range(0,int(len(sem2)),2):
                s:list = []
                s.append(int(sem2[i]))
                s.append(int(sem2[i+1])-1+int(sem2[i]))
                sem.append(s)
            print(sem)
            for i in range(1,6):
                cis = []
                radky:list = soubor[i].split('\n')
                radky.pop(0)
                for x in radky:
                    c2:list = x.split(' ')
                    c:list = []
                    for y in c2:
                        c.append(y)
                    cis.append(c)
                sem = uprav(sem,cis)
                print("prevedeno")
                print(sem)
            print(min(sem))
            
parse("test.txt")
