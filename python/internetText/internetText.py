<<<<<<< HEAD
from os.path import realpath, dirname, join
import urllib.request
import random
def novySoubor(jmeno):
    cislo = str(random.randrange(0,70000))
    s = "https://www.gutenberg.org/cache/epub/"+cislo+"/pg"+cislo+".txt"
    print(s)
    with urllib.request.urlopen(s) as web:
        data = web.read().decode("utf-8")
    nazev = jmeno+".txt"
    print(nazev)
    with open(join(dirname(realpath(__file__)),nazev),"w", encoding="utf_8") as file:
        file.write(str(data))
novySoubor("randomkniha")
=======
from os.path import realpath, dirname, join
import urllib.request
import random
def novySoubor(jmeno):
    cislo = str(random.randrange(0,70000))
    s = "https://www.gutenberg.org/cache/epub/"+cislo+"/pg"+cislo+".txt"
    print(s)
    with urllib.request.urlopen(s) as web:
        data = web.read().decode("utf-8")
    nazev = jmeno+".txt"
    print(nazev)
    with open(join(dirname(realpath(__file__)),nazev),"w", encoding="utf_8") as file:
        file.write(str(data))
novySoubor("randomkniha")
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
