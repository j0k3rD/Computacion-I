from constants import Constants as constants
import sys
from bank import Bank

class Main:
    #Variable de Clase
    #Funcion Menu
    def menu():
        #Instanciar el que realiza metodos
        b = Bank()
        while True:
            print(constants.MENU)
            opc = int(input(constants.ANSWER))
            
            if opc == 1:

                print(constants.SPACE)
                b.add_client()
                b.register_data()
                print(constants.SPACE)
                input(constants.P_TO_C)

            elif opc == 2:

                print(constants.SPACE)
                b.add_client_to_queue()
                b.register_data()
                input(constants.P_TO_C)

            elif opc == 3:

                print(constants.SPACE)
                b.call_client()
                b.register_data()
                input(constants.P_TO_C)


            elif opc == 4:

                print(constants.SPACE)
                b.show_register()
                input(constants.P_TO_C)

            elif opc == 5:
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