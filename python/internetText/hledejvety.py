<<<<<<< HEAD
from os.path import realpath, dirname, join
import re
reg2:str = "[A-Z][!-@a-z\s][^.!?]+\s"
reg:str  = "[A-Z][!-@a-z\s][^.!?]*\.\s"
text:str = "Imagine have the chance to meet Dr. House. He was with Mr. Home. I have the chance to meet Dr. House. He was with Mr. Home. Au. "
with open(join(dirname(realpath(__file__)),"kniha.txt"),"r", encoding="utf_8") as file:
    text:str = ""
    text = text.join(str(line) for line in file.read().split("\n")[94:19171])
    soubor:list = file.read().split("\n")
    print(len(soubor))
    #print(text)
    x = re.findall(reg,text)
#print(x)
pocet:int = len(x)
print(pocet)
tituly:list = []
for z in x:
    titul = re.findall("\s[A-Z][!-@a-z]{,2}\.",z)
    if len(titul) > 0:
        pocet -=1
print(pocet)
=======
from os.path import realpath, dirname, join
import re
reg2:str = "[A-Z][!-@a-z\s][^.!?]+\s"
reg:str  = "[A-Z][!-@a-z\s][^.!?]*\.\s"
text:str = "Imagine have the chance to meet Dr. House. He was with Mr. Home. I have the chance to meet Dr. House. He was with Mr. Home. Au. "
with open(join(dirname(realpath(__file__)),"kniha.txt"),"r", encoding="utf_8") as file:
    text:str = ""
    text = text.join(str(line) for line in file.read().split("\n")[94:19171])
    soubor:list = file.read().split("\n")
    print(len(soubor))
    #print(text)
    x = re.findall(reg,text)
#print(x)
pocet:int = len(x)
print(pocet)
tituly:list = []
for z in x:
    titul = re.findall("\s[A-Z][!-@a-z]{,2}\.",z)
    if len(titul) > 0:
        pocet -=1
print(pocet)
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
