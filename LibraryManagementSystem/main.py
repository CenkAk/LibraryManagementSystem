import datetime
import os
import sys

class Library:
    """ Bu sinif kutuphanedeki kitaplarin kayitlarini tutar.
    3 module sahip: "Listeleme", "Kaldirma", "Ekleme" """

    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self): 
        self.file.close()

    def list_books(self):
         self.file.seek(0)
         books = self.file.read().splitlines()
         for book in books:
            book_info = book.split(',')
            print(f"Kitap: {book_info[0]}, Yazar: {book_info[1]},")

    def add_book(self):
        title = input("Kitap adini girin: ")
        author = input("Kitap yazarini girin: ")
        release_year = input("Kitap yayin yilini girin: ")
        pages = input("Kitap sayfa sayisini girin: ")

        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Kitap eklendi!")
    
    def remove_book(self, title_to_remove):
        self.file.seek(0) 
        books = self.file.read().splitlines()

        found = False
        updated_books = []
        for book in books:
            book_info = book.split(',')
            if book_info[0] != title_to_remove:
                updated_books.append(book)
            else:
                found = True

        if found:
            self.file.seek(0)
            self.file.truncate()
            for book in updated_books:
                self.file.write(book + '\n')
            print(f"'{title_to_remove}' adli kitap kaldirildi.")
        else:
            print(f"'{title_to_remove}' adli bir kitap bulunamadi.")

example_books = [
    "Tutunamayanlar,Oguz Atay,2000,724",
    "Yuzuklerin Efendisi 1,J.R.R Tolkien,1954,520"
]

with open("books.txt", "w") as file:
    for book in example_books:
        file.write(book + "\n")


while True:
    lib = Library()
    print("\n*** MENU ***")
    print("1) Kitaplari Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldir")
    print("4) Cikis")
    
    choice = input("Seciminizi Yapin (1-4): ")
    
    if choice == "1":
        print("\nKitaplarin Listesi:")
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        title_to_remove = input("Kaldirmak istediginiz kitabin adini girin: ")
        lib.remove_book(title_to_remove)
    elif choice == "4":
        break
    else:
        print("Bir seyler yanlis gitti!")


#Normalde asagidaki gibi yapmak istedik ama surekli  
#Exception ignored in: <function Library.__del__ at 0x000001DDE13DD3A0>
#File "c:\Users\Cenkk\Documents\PYTHON ODEV\main.py", line 13, in __del__
    #self.file.close()
    #^^^^^^^^^
#AttributeError: 'Library' object has no attribute 'file'
#Bir seyler yanlis gitti! 

#hatasi aldik o yuzden daha farkli bir menu kullandik"""

"""try:
    lib = Library("books.txt")
    press_key_list = {"E": "Kitap Ekle", "K": "Kitap Kaldir", "L": "Kitap Listele", "Backspace": "Cikis"}
    key_press = False
    while not (key_press == "Backspace"):
        print(f"\n *** MENU***\n")
        for key, value in press_key_list.items():
            print(value, "'ya erismek icin", key, "basin!")
            key_press = input("Tusa Basin: ").lower()
            if key_press == "e":
                print("\nSunu sectiniz: Kitap Ekle\n")
                lib.add_book()
            elif key_press == "k":
                print("\nSunu sectiniz: Kitap Kaldirma\n")
                lib.remove_book()
            elif key_press == "l":
                print("\nSunu sectiniz: Kitap Listeleme\n")
                lib.list_books()
            elif key_press == "\b":
                break
            else:
                continue
except Exception as e:
    print("Bir seyler yanlis gitti!")"""