from os.path import realpath, dirname, join
def frombin(l:dict)->int:
    v = ""
    for c in l.values():
        v+=c
    mocnina = 1
    vysledek = 0
    for cislo in v:
        vysledek+= mocnina*int(cislo)
        mocnina = mocnina*2
    print(vysledek)
    return vysledek
def evaluate(w:list,g:list):
    while g != []:
        for gate in g:
            if gate[0] in w.keys() and gate[2] in w.keys() and gate[3] not in w.keys():
                match gate[1]:
                    case "AND":
                        if w[gate[0]] == "1" and w[gate[2]] == "1":
                            w[gate[3]] = "1"
                        else:
                            w[gate[3]] = "0"
                    case "OR":
                        if w[gate[0]] == "0" and w[gate[2]] == "0":
                            w[gate[3]] = "0"
                        else:
                            w[gate[3]] = "1"
                    case "XOR":
                        if w[gate[0]] == w[gate[2]]:
                            w[gate[3]] = "0"
                        else:
                            w[gate[3]] = "1"
                g.pop(g.index(gate))
    print(w)
def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        soubor = file.read().split("\n\n")
        wires_s = soubor[0]
        wires = {}
        for line in wires_s.split("\n"):
            key = line.split(": ")[0]
            value = line.split(": ")[1]
            wires[key] = value
        gates_s = soubor[1]
        gates = []
        for line in gates_s.split("\n"):
            gate = line.split(" ")
            gate.pop(3)
            gates.append(gate)
        # print(wires)
        xs = {}
        for w in wires.keys():
            if w[0] == "x":
                xs[w] = wires[w]
        # print(xs)
        sorted_xs = dict(sorted(xs.items()))
        ys = {}
        for w in wires.keys():
            if w[0] == "y":
                ys[w] = wires[w]
        # print(ys)
        sorted_ys = dict(sorted(ys.items()))
        # print(gates)
        evaluate(wires,gates)
        zs = {}
        for w in wires.keys():
            if w[0] == "z":
                zs[w] = wires[w]
        # print(zs)
        sorted_zs = dict(sorted(zs.items()))
        print(sorted_xs)
        dec_xs = frombin(sorted_xs)
        print(sorted_ys)
        dec_ys = frombin(sorted_ys)
        print(sorted_zs)
        dec_zs = frombin(sorted_zs)
        corect_dec_zs = dec_xs + dec_ys
        print(corect_dec_zs)
        # corect_ys = tobin(corect_dec_zs)

parse("input.txt")