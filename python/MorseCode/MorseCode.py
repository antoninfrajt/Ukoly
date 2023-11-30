from os.path import join, dirname, realpath
Abeceda:list=[]
def ZapisAbecedu(soubor:str,l:list):
    with open(join(dirname(realpath(__file__)),soubor),"r", encoding="utf_8") as file:
            for line in file.read().split('\n'):
                  l.append(line)
def Preloz(t:str,l:list):
      PrelozenyText:str="//"
      for x in t:
            for y in l:
                  if x==y[0] or str.upper(x)==y[0]:
                        PrelozenyText+=y[2:]+"//"
            if x==" ":
                  PrelozenyText+="/"
      print(PrelozenyText)
ZapisAbecedu("MorseCode.txt",Abeceda)
text:str = input("Zadejte prekladany text.")
Preloz(text,Abeceda)


