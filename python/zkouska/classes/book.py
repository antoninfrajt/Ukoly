<<<<<<< HEAD
class Book:
    def __init__(self,s:str):
        self.id = int(s.split(";")[0])
        self.name = s.split(";")[1]
        self.author = s.split(";")[2]
        if s.split(";")[3] == "Available":
            self.available = True
        else:
            self.available = False
    def __str__(self)->str:
        s = str(self.id) + ";" + self.name + ";" + self.author + ";"
        if self.available:
            s += "Available"
        else:
            s += "Unavailable"
        return s
    def __lt__ (self,other):
        if self.author [0] < other.author[0]:
            return True
        else:
            return False
    def __eq__(self, other) -> bool:
        if self.id == other.id:
            return True
        else:
            return False
    def set_id(self, id):
        self.id = id

=======
class Book:
    def __init__(self,s:str):
        self.id = int(s.split(";")[0])
        self.name = s.split(";")[1]
        self.author = s.split(";")[2]
        if s.split(";")[3] == "Available":
            self.available = True
        else:
            self.available = False
    def __str__(self)->str:
        s = str(self.id) + ";" + self.name + ";" + self.author + ";"
        if self.available:
            s += "Available"
        else:
            s += "Unavailable"
        return s
    def __lt__ (self,other):
        if self.author [0] < other.author[0]:
            return True
        else:
            return False
    def __eq__(self, other) -> bool:
        if self.id == other.id:
            return True
        else:
            return False
    def set_id(self, id):
        self.id = id

>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
