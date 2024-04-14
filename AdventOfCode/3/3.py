from os.path import realpath, dirname, join
import re
def JeSpecSymbol(s:str):
    if s.isdigit() == True or s == ".":
        return False
    else:
        return True
def JeSoucastka(c:str,r:list,v:list)->dict:
    print("hledam:"+c)
    pocet:int = 0
    idxr:int = 0
    soucastka:bool = False
    for rad in r:
        cisrad:list = []
        newy:str = ""
        cisrad = re.findall("[0-9]+",rad)
        doc = rad
        for x in cisrad:
            if x==c:
                print("fnc jede")
                idxp:int = rad.find(c)
                rad = rad[:idxp]+"x"+rad[idxp+1:]
                doc = rad
                for x in c:
                    pispred:int = 0
                    pispo:int = 0
                    print("cast:"+x)
                    okoli:str = ""
                    #print(str(idxp))
                    pispred = idxp-1
                    if pispred < 0:
                        #print("jdu mimo tabulku")
                        pispred = idxp
                    pispo = idxp+1
                    if pispo >= len(rad):
                        #print("jdu mimo tabulku")
                        pispo = idxp
                    radpred = idxr-1
                    if radpred < 0:
                        #print("jdu mimo tabulku")
                        radpred = idxr
                    radpo = idxr+1
                    if radpo >= len(r):
                        #print("jdu mimo tabulku")
                        radpo = idxr
                    txt:str = okoli.join([r[radpred][pispred],r[radpred][idxp],r[radpred][pispo],r[idxr][pispred],r[idxr][pispo],r[radpo][pispred],r[radpo][idxp],r[radpo][pispo]])
                    #if JeSpecSymbol(r[radpred][pispred]) or JeSpecSymbol(r[radpred][idxp]) or JeSpecSymbol(r[radpred][pispo]) or JeSpecSymbol(r[idxr][pispred]) or JeSpecSymbol(r[idxr][pispo]) or JeSpecSymbol(r[radpo][pispred]) or JeSpecSymbol(r[radpo][idxp]) or JeSpecSymbol(r[radpo][pispo]):
                    print(txt)
                    for i in txt:
                        if JeSpecSymbol(i):
                            print("ano")
                            soucastka = True
                    idxp += 1
                print(rad)
                if soucastka == True:
                    if c not in v:
                        v.append(int(c))
                        pocet += 1
                        print("mame")
                        print("radek:"+str(idxr+1))
                        print(cisrad) 
                soucastka = False
            else :
                rad = doc.replace(x,"."*len(x))
                #print(rad)
                doc = rad       
        idxr += 1
    print(str(pocet)+"*"+c)
    return v
def parse(s:str):
    obs:list = []
    Vys:list = []
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            soubor:list = file.read().split('\n')
            radky:list = []
            cisla:list = []
            bordel:list = []
            soucet:int = 0
            znak:bool = False
            for x in soubor:
                cisla.extend(re.findall("([0-9]+)",x))
                radky.append(x)
                newy:str = ""
                for z in x:
                    if JeSpecSymbol(z):
                        if z not in bordel:
                            bordel.append(z)
                cisla2:list = []
                for cislo in cisla:
                    if cislo not in cisla2:
                        cisla2.append(cislo)
                cisla = cisla2
            print("cisla")
            #print(cisla)
            cisla.sort()
            for c in cisla:
                Vys = JeSoucastka(c,radky,Vys)
            soucet += sum(Vys)
            print("finalni soucet je:"+str(soucet))
            Vys.sort()
            print(cisla)
            print(Vys)
            print(bordel)
parse("input.txt")
if JeSpecSymbol("*"):
    print("ano")




