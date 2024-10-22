import statistics
def Vynasobcisla (c:list)->int:
    v = 1
    for cislo in c:
        v = v*cislo
    return v

def PracujSCisly()->None:
    strcisla:list = input("Zadejte cisla ve formatu #,#,#...:").split(",")
    cisla:list[int] = []
    for strcislo in strcisla:
        c = int(strcislo)
        cisla.append(c)
    soucet = sum(cisla)
    soucin = Vynasobcisla(cisla)
    prumer = round(sum(cisla)/len(cisla),2)
    median = statistics.median(cisla)
    print("Soucet je " + str(soucet) + "\nSoucin je " + str(soucin) + "\nPrumer je " + str(prumer) + "\nMedian je " + str(median))

PracujSCisly()
