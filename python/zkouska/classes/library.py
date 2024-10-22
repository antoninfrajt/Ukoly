from os.path import realpath, dirname, join
from classes.book import Book
class Library:
    def __init__(self,s):
        self.path = s
        self.library = []
        with open(join(dirname(realpath(__file__)),s),"r", encoding="utf_8") as file:
            for line in file.read().split("\n"):
                b = Book(line)
                self.library.append(b)
        self.library.sort()
    def __str__(self):
        s = ""
        for b in self.library:
            s += b.__str__() + "\n"
        return s
    def add_book(self,book):
        new_book = book
        unique = True
        for b in self.library:
            if b == book:
                unique = False
        if unique:
            self.library.append(book)
            print("Kniha byla přidána s ID: " + str(book.id))
        else:
            print("Kniha nemá unikátní ID")
    def get_unique_id(self):
        id = 1
        used_ids = []
        for b in self.library:
            used_ids.append(b.id)
        used_ids.sort()
        for i in used_ids:
            if i == id:
                id+= 1
        return id
    def show_available_books(self):
        available_books = []
        for b in self.library:
            if b.available == True:
                available_books.append(b)
        s= ""
        for b in available_books:
            s += b.__str__() + "\n"
        print(s)
    def find_book_and_borrow_it(self,name):
        find = []
        for b in self.library:
            if name in b.name and b.available == True:
                find.append(b)
        if len(find) == 0:
            print("Nenalezena žádná dostupná kniha s tímto jménem.")
        elif len(find) > 1:
            print("Nalezeno více knih, prosím upřesněte hledání:")
            s = ""
            for b in find:
                s += b.__str__() + "\n"
            print(s)
        else:
            print("nalezena tato kniha:")
            print(find[0])
            print("Chcete knihu vypujcit? (A/N)")
            if input() == "A":
                print("Kniha vypůjčena")
                for b in self.library:
                    if find[0].name == b.name:
                        b.available = False
                        print(b.available)
            else:
                print("Kniha nebyla vypůjčena.")
                pass



                   