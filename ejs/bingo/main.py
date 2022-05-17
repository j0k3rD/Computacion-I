from constants import Constants as constants
from program import Program
from bingo import Bingo


class Main:
    #Variable de Clase
    #Funcion Menu
    def main():
        #Instanciar el que hace todo
        p = Program()
        while True:
            print(constants.MENU)
            opc = int(input(constants.ANSWER))
            
            if opc == 1:

                print(constants.SPACE)
                p.generate_bingo()
                print(constants.SPACE)
                input(constants.P_TO_C)

            # elif opc == 2:

            #     print(constants.SPACE)
            #     input(constants.P_TO_C)

            # elif opc == 3:

            #     print(constants.SPACE)
            #     input(constants.P_TO_C)


            # elif opc == 4:

            #     print(constants.SPACE)
            #     input(constants.P_TO_C)

            elif opc == 5:
                print(constants.WANT_QUIT)
                op = int(input(constants.ANSWER))
                if op == 1:
                    print(constants.EXITING)
                    break
                elif op == 2:
                    print(constants.RETURNING)
                    Main.main()
                else:
                    print(constants.INV_OP)
            else:
                print(constants.INV_OP2)

if __name__ == "__main__":
    Main.main()