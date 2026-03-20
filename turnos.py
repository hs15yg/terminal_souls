RED = '\033[31m'
RESET = '\033[0m'
AMARILLO = '\033[33m'
BLANCO = '\033[37m'
AZUL = '\033[34m'
import os
import time
import headers


def turno_jugador():
    interupt = True
    while interupt:
        os.system('clear') 
        
        print(f"Turno del Jugador:\nOpciones:\n\n1. {headers.colors["RED"]}Atacar{headers.colors["RESET"]}\n2. {headers.colors["WHITE"]}Curar{headers.colors["RESET"]}\n3. {headers.colors["BLUE"]}Habilidad Especial{headers.colors["RESET"]}\n4. {headers.colors["YELLOW"]}Pasar Turno{headers.colors["RESET"]}")
        try:    
            op = int(input("Elegir acción -> "))
            if op == 1:
                print("Atacar")
                interupt = False
            elif op == 2:
                print("Curar")
                interupt = False
            elif op == 3:
                print("Habilidad Especial")
                interupt = False
            else:
                os.system('clear') 
                print(f"{RED}[x]{RESET} Deber elegir una opcion valida!")
                time.sleep(1)

        except:
            os.system('clear') 
            print(f"{RED}[x]{RESET} Revisa que estes insertando datos numericos")
            time.sleep(1)


turno_jugador()