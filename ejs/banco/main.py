from queue import Queue
from box import Box
from client import Client
from bank import Bank


class Main:
    #Variable de Clase
    #Funcion Menu
    def main():
        b = Bank()

        while True:
            print("""
                    Select an Option:

                    1. Add New Clients.
                    2. Add Client to Queue
                    3. Call a New Client.
                    4. See Queues and Boxes Stats.
                    5. Exit.

                    """)

            opc = int(input("Option: "))
            
            if opc == 1:
                b.add_client()
                print("\n")
                b.add_to_register()
                print("\n")
                input("Press a key to Continue..")

            elif opc == 2:
                b.add_client_to_queue()
                b.add_to_register()
                print("\n")
                input("Press a key to Continue..")

            elif opc == 3:
                b.call_verify_client_in_queue()
                b.add_to_register()
                print("\n")
                input("Press a key to Continue..")


            elif opc == 4:
                b.show_queue_stats()
                print("\n")
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

## LAS CLASES CON PRIMERA LETRA MAY
## CONSTANTES TODO(to do) MINUSCULA
## FUNCIONES, VARIABLES, ARCHIVOS MINUSCULA
## ARCHIVOS.TXT MINUSCULA