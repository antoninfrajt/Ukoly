import re
from os.path import realpath, dirname, join

def parse(s):
    soucet = 0
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        text:str = file.read()
        seznam = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)",text)
        multyply = True
        for i in seznam:
            if i == "don't()":
                multyply = False
                i = " "
            elif i == "do()":
                multyply = True
                i = " "
            if i != " " and multyply:
                cisla = i[4:-1]
                print(cisla)
                soucet += int(cisla.split(',')[0]) * int(cisla.split(',')[1])
                print(soucet)
    # print(seznam)
parse("input.txt")