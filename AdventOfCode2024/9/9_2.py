from os.path import realpath, dirname, join

def parse(s:str):
    with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
        s= file.read()
        print(s)
        news = []
        id = 0
        idx = 1
        idmax = int((len(s))/int(2))
        print(idmax)
        for c in s:
            if idx%2 != 0:
                
                news.append(list([id,int(c)]))
                id += 1
            else:
                
                news.append(list([".",int(c)]))
            idx += 1
        print(news)
        print()
        for i in range(0,idmax):
            id = idmax-i
            # print(id)
            for s in news:
                if s[0] == id:
                    idx = 0
                    for d in news:
                        if d[0] == "." and d[1]>= s[1]:
                            if d[1] > s[1]:
                                news[news.index(s)] = list([".",s[1]])
                                news[idx][1] = d[1] - s[1]
                                news.insert(idx,s)
                                # print(news)
                                break
                            else:
                                
                                news[news.index(s)] = list([".",s[1]])
                                news[idx] = s
                                # print(news)
                                break 
                        idx += 1
        print (news)
        vysledek = 0
        idx = 0
        string = []
        for s in news:
            for i in range(0,s[1]):
                string.append(s[0])
        for s in string:
            if s != ".":
                vysledek += idx*s
            idx+= 1
        print(vysledek)


parse("test.txt")