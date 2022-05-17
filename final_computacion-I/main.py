from dbm.ndbm import library
from constants import Constants as constants
from library import Library
import sys


class Main:
    #Variable de Clase
    #Funcion Menu
    def menu():
        #Instanciar el que realiza metodos
        library = Library()
        while True:
            print(constants.MENU)
            opc = int(input(constants.ANSWER))
            
            if opc == 1:

                print(constants.SPACE)
                library.add_book()
                print(constants.SPACE)
                input(constants.P_TO_C)

            elif opc == 2:

                print(constants.SPACE)
                library.add_client()
                input(constants.P_TO_C)

            elif opc == 3:

                print(constants.SPACE)
                library.show_clients()
                input(constants.P_TO_C)


            elif opc == 4:
                print(constants.WANT_QUIT)
                op = int(input(constants.ANSWER))
                if op == 1:
                    print(constants.EXITING)
                    sys.exit(0)
                elif op == 2:
                    print(constants.RETURNING)
                    Main.menu()
                else:
                    print(constants.INV_OP)
            else:
                print(constants.INV_OP2)

if __name__ == "__main__":
    Main.menu()