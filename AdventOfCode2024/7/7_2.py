from os.path import realpath, dirname, join
import itertools, string

def calculate(c:list):
    soucet = 0
    for r in c:
        ok = False
        moznosti = []
        cil = r[0]
        kombo = itertools.product(['+','*',"|"],repeat=len(r[1])-1)
        s= ""
        # for c in kombo:
        #     s += str(c) + " "
        # print(s)
        for d in kombo:
            # print(d)
            # print(len(d))
            moznost = list(r[1])
            for i in range(0,len(d)):
                moznost.insert(i*2+1,d[i])
                # print(moznost)
                # print(r[1])
            moznosti.append(moznost)
        # print(moznosti)
        for m in moznosti:
            vysledek = int(m[0])
            idx = 0
            for c in m:
                if c in string.punctuation and c != " ":
                    match c:
                        case "+":
                            vysledek += int(m[idx+1])
                        case "*":
                            vysledek = vysledek*int(m[idx+1])
                        case "|":
                            s = str(vysledek)
                            s += m[idx+1]
                            vysledek = int(s)
                # print(vysledek)
                # print(cil)
                idx += 1
            if vysledek == int(cil):
                ok = True
                break
        if ok:
            soucet += int(cil)
            print(cil)
            print(soucet)

                

def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        cal = []
        for line in file.read().split("\n"):
            # text = line.split(":")
            radek = list([line.split(": ")[0],line.split(": ")[1].split(" ")])
            cal.append(radek)
    calculate(cal)

parse("test.txt")
