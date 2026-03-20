RED = '\033[31m'
RESET = '\033[0m'
AMARILLO = '\033[33m'
BLANCO = '\033[37m'
AZUL = '\033[34m'
import os
import time
import headers


def player_turn():
    interupt = True
    while interupt:
        os.system('clear') 
        
        print(f"Player Turn:\nOptions:\n\n1. {headers.colors["RED"]}Attack⚔️{headers.colors["RESET"]}\n2. {headers.colors["WHITE"]}Cure💊{headers.colors["RESET"]}\n3. {headers.colors["BLUE"]}Special Ability✨{headers.colors["RESET"]}\n4. {headers.colors["YELLOW"]}Dodge💨{headers.colors["RESET"]}")
        try:    
            op = int(input("Choice action -> "))
            if op == 1:
                print("Attack")
                interupt = False
            elif op == 2:
                print("Cure")
                interupt = False
            elif op == 3:
                print("special ability")
                interupt = False
            else:
                os.system('clear') 
                print(f"{RED}[x]{RESET} you must choose a valid option")
                time.sleep(1)

        except:
            os.system('clear') 
            print(f"{RED}[x]{RESET} check that they are entering numerical data")
            time.sleep(1)


player_turn()