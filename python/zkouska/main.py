<<<<<<< HEAD
from classes.book import Book
from classes.library import Library

def main():
    print("jede")
    book = Book("9;Animal Farm;Orwell George;Available")
    print(book)
    print()

    library = Library("data.txt")
    print(library)
    print()

    library.add_book(book)
    print()    

    book.set_id(library.get_unique_id())
    library.add_book(book)
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

    print("Půjčení knihy:")
    library.find_book_and_borrow_it("Kill")
    print()
    library.find_book_and_borrow_it("a")
    print()
    library.find_book_and_borrow_it("Great")
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

main()
=======
from classes.book import Book
from classes.library import Library

def main():
    print("jede")
    book = Book("9;Animal Farm;Orwell George;Available")
    print(book)
    print()

    library = Library("data.txt")
    print(library)
    print()

    library.add_book(book)
    print()    

    book.set_id(library.get_unique_id())
    library.add_book(book)
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

    print("Půjčení knihy:")
    library.find_book_and_borrow_it("Kill")
    print()
    library.find_book_and_borrow_it("a")
    print()
    library.find_book_and_borrow_it("Great")
    print()

    print("Dostupné knihy:")
    library.show_available_books()
    print()

main()
>>>>>>> 5416915f6e236b2c4f9e3ce51dee2d4b630d547c
