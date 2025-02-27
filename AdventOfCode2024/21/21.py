from os.path import realpath, dirname, join
def translate(move:list,znak:str)->list[str]:
    outputs = []
    x = move[0]
    y = move[1]
    output = ""
    if x > 0:
       for i in range(0,x):
           output+= ">"
    if x < 0:
        x = -x
        for i in range(0,x):
            output += "<"
        x=-x
    if y < 0:
        y = -y
        for i in range(0,y):
            output += "^"
        y = -y
    if y > 0:
        for i in range(0,y):
            output += "v"  
    output+= "A"
    outputs.append(output)
    output = ""
    if y < 0:
        y = -y
        for i in range(0,y):
            output += "^"
        y = -y
    if y > 0:
        for i in range(0,y):
            output += "v"
    if x > 0:
       for i in range(0,x):
           output+= ">"
    if x < 0:
        x = -x
        for i in range(0,x):
            output += "<"
        x=-x  
    output+= "A"
    if output not in outputs:
        outputs.append(output)
        for o in outputs:
            if o != "A":
                if znak == "0" and o[0] == "<":
                    outputs.pop(outputs.index(o))
                elif znak == "A" and o[1] == "<":
                    outputs.pop(outputs.index(o))
                elif znak == "1" and o[0] == "v":
                    outputs.pop(outputs.index(o))
                elif znak == "4" and o[1] == "v":
                    outputs.pop(outputs.index(o))
                elif znak == "7" and o[2] == "v":
                    outputs.pop(outputs.index(o))
                elif znak == "^" and o[0] == "<":
                    outputs.pop(outputs.index(o))
                elif znak == "<" and o[0] == "^":
                    outputs.pop(outputs.index(o))
    # print(outputs)
    return outputs
def instructions(s:str,pad:dict)->list:
    instruct:list[str] = []
    instruction = ""
    pos = pad["A"]
    idx = 0
    pred = "A"
    for znak in s:
        # print(pred)
        # print(idx)
        move = list([pad[znak][0]-pos[0],pad[znak][1]-pos[1]])
        if idx == 0:
            # print(translate(move,pred))
            for m in translate(move,pred):
                instruct.append(m)
                # print(instruct)
        else:
            if len(translate(move,pred)) == 1:
                for i in range(0,len(instruct)):
                    # print(translate(move)[0])
                    instruct[i] += translate(move,pred)[0]
                # print(instruct)
            else:
                # print(translate(move))
                for i in list(instruct):
                    instruct.append(i)
                # print(instruct)
                for i in range(0,len(instruct)):
                    instruct[i] += translate(move,pred)[i%2]
        pos = pad[znak]
        pred = znak
        idx+= 1
        # print(instruct)
    return instruct


def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        codes = file.read().split("\n")
        repeat = 3
        numpad = {"7":[0,0],"8":[1,0],"9":[2,0],"4":[0,1],"5":[1,1],"6":[2,1],"1":[0,2],"2":[1,2],"3":[2,2],"0":[1,3],"A":[2,3]}
        d_pad = {"^":[1,0],"A":[2,0],"<":[0,1],"v":[1,1],">":[2,1]}
        button_ord = []
        complexity = 0
        for c in codes:
            print(c)
            for i in range(0,repeat):
                if i == 0:
                    c = instructions(c,numpad)
                else:
                    newc = []
                    for code in c:
                        # print(instructions(code,d_pad))
                        for inst in instructions(code,d_pad):
                            # print(inst)
                            newc.append(inst)
                        # print("newc")
                        # print(newc)
                    c = list(newc)
                    # print(c)
            velikost = []
            for cislo in c:
                velikost.append(len(cislo))
            print(velikost)
            print(min(velikost))
            upload = c[0]
            # print("upload")
            # print(upload)
            for inst in c:
                if len(inst) < len(upload):
                    print("yes")
                    print(str(len(upload)) + " " + str(len(inst)))
                    upload = inst
                    print(upload)
            button_ord.append(upload)
        print(button_ord)
        for i in range(0,len(codes)):
            complexity += len(button_ord[i])*int(codes[i][:len(codes[i])-1])
            print(str(len(button_ord[i])) + "*" + codes[i][:len(codes[i])-1])
        print(complexity)



parse("test.txt")
# [^A] [^^<<A] [>>A] [vvvA]
# [<A >A] [<A A v<A A >>^A] [vA A ^A] [v<A A A >^A]
# [v<<A >>^A vA ^A] [v<<A >>^A A v<A <A >>^A A vA A ^<A >A] [v<A >^A A <A >A] [v<A <A >>^A A A vA ^<A >A]
# [^A] [<<^^A] [>>A] [vvvA]
# [<A >A] [v<<A A >^A A >A] [vA A ^A] [<vA A A >^A]
# [<v<A >>^A vA ^A] [<vA <A A >>^A A vA <^A >A A vA ^A] [<vA >^A A <A >A] [<v<A >A >^A A A vA <^A >A]