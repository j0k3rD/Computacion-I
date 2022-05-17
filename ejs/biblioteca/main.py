from book import Book
from author import Author
from reader import Reader
from library import Library

class Main:
    def main():
        l = Library()

        while True:
            print("""
                    Select an Option:

                    1. Add an Author.
                    2. Add a Book.
                    3. Add a Reader.
                    4. Borrow a Book.
                    5. Exit.

                    """)
            opc = int(input("Option: "))
            
            if opc == 1:
                l.addAuthor(Author(input("Enter the Author's Name: "), input("Enter the Nacionality: "), input("Enter Birthday: ")))
                print("\n")
                l.viewAuthor()
                input("Press a key to Continue..")

            elif opc == 2:
                l.viewBook()

                l.addBook(Book(input("Enter the Book's Name: "), input("Enter the Type: "), input("Enter the Editorial: "), input("Enter the Year: "), input("Enter the Author: ")))
                l.viewBook()
                input("Press a key to Continue..")

            elif opc == 3:
                l.addReader(Reader(input("Enter the Name: "), input("Enter new Borrow: ")))
                input("Press a key to Continue..")

            elif opc == 4:
                l.addBorrowed()
                input("Press a key to Continue..")
            elif opc == 5:
                print("""
                        Are you sure you want to go out? 
                        1.Yes
                        2.No
                        """)
                op = int(input("Enter the option: \n"))
                if op == 1:
                    print("Exiting..")
                    break
                elif op == 2:
                    print("Returning..")
                    Main.main()
                else:
                    print("Invalid Option")
            else:
                print("Enter a Correct Option!, Try again..")

if __name__ == "__main__":
    Main.main()