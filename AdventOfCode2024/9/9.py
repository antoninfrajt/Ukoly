from os.path import realpath, dirname, join

def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        s= file.read()
        print(s)
        news = []
        id = 0
        idx = 1
        for c in s:
            if idx%2 != 0:
                for i in range(0,int(c)):
                    news.append(id)
                id += 1
            else:
                for i in range(0,int(c)):
                    news.append(".")
            idx += 1
        print(news)
        print()
        idx = 0
        for s in news:
            if s == ".":
                # print(idx)
                # print(news[:idx])
                # print(news[-1])
                # print(news[idx+1:len(news)-1])
                news[idx] = news[-1]
                news.pop()
                while news[-1] == ".":
                    news.pop()
                # print(news)
                # print("\n")
            idx += 1
            if "." not in news:
                break
        print (news)
        vysledek = 0
        idx = 0
        for s in news:
            vysledek += idx*s
            idx+= 1
        print(vysledek)


parse("test.txt")