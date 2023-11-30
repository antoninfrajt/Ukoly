def kmen(sirka:int,vyska:int,vk:int):
    for i in range(0,vk):
        print(" "*(vyska-(int(sirka/2))-1),"#"*(sirka))

def koruna(vyska:int,):
    for i in range(0,vyska+1):
        print(" "*(vyska-i),"*"*(i*2-1))
def stromek(vyska:int, sirka:int,vk:int):
    koruna(vyska)
    kmen(sirka,vyska,vk)
vyska = int(input("zadejte vysku stromku:"))
vysKmen = int(input("zadejte vysku kmene:"))
sirka = int(input("zadejte sirku stromku:"))
stromek(vyska,sirka,vysKmen)



