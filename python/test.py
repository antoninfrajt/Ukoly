print("zadejte heslo")
h = str(input())
velkepismeno = False
cislo = False
malepismeno = False
s = False
for i in h:
    if i.isnumeric():
        cislo = True
    if ord(i) >= 65 and ord(i) <= 90:
        velkepismeno = True
    if ord(i) >= 97 and ord(i) <= 122:
        malepismeno = True
if velkepismeno and malepismeno and cislo and len(h) >= 8 :
    s = True
if s:
    print("Platne")
else:
    print("Neplatne")


