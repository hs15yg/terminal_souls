import os
import time

colors = {
    "RED": "\033[31m",
    "BLACK": "\033[30m",
    "YELLOW": "\033[33m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "RESET": "\033[0m",
    "WHITE": "\033[37m",
}

player = {
    "hp": 100,
    "name" : "",
    "potions": 3
}

enemy1 = {
    "hp": 120,
    "name" : "Enemy 1",
    "potions": 3
}

o_system = ["clear"]

# i create a function called start
def start():
    print(f"\n{colors['YELLOW']}========================================{colors['RESET']}")
    print(f"{colors['WHITE']}       🛡️  MENU - TERMINAL SOULS  🛡️{colors['RESET']}")
    print(f"{colors['YELLOW']}========================================{colors['RESET']}")
    
    option = 0
    while option != 1 and option != 2:
        try:
            # Menu option
            print(f"\n{colors['BLUE']}  [1]{colors['RESET']} Play Game")
            print(f"{colors['BLUE']}  [2]{colors['RESET']} Exit")
            
            option = int(input(f"\n{colors['YELLOW']}➜ Selection: {colors['RESET']}"))
        except:
            print(f"{colors['RED']}⚠️  Error: Enter only numbers!{colors['RESET']}")

    if option == 1:
        os.system(o_system[0])
        print(f"\n{colors['GREEN']}✨ Welcome to the world of Terminal Souls! ✨{colors['RESET']}")
        name = input(f"{colors['WHITE']}✍️  Enter your name: {colors['RESET']}")
        
        print(f"\n{colors['RED']}🔥 Get ready, {name}!{colors['RESET']}")
        print(f"{colors['YELLOW']}The battle begins now...{colors['RESET']}\n")
        
        player["name"] = name
        return True
    else:
        print(f"\n{colors['WHITE']}➜] You have left the game. Farewell!{colors['RESET']}\n")
        os.system(o_system[0])
        return False
    
def win():

    os.system(o_system[0])
    print(f"\n{colors['RED']}💥 {enemy1['name']} has been defeated!{colors['RESET']}")
    time.sleep(1.5)

    os.system(o_system[0])
    print(f"\n{colors['YELLOW']}✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨{colors['RESET']}")
    print(f"{colors['WHITE']}       🏆  VICTORY ACHIEVED!  🏆{colors['RESET']}")
    print(f"{colors['YELLOW']}✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨{colors['RESET']}")
    time.sleep(1)

    os.system(o_system[0])
    print(f"\n{colors['GREEN']}╔══════════════════════════════════════════╗{colors['RESET']}")
    print(f"║                                          ║")
    print(f"║   {colors['WHITE']}The brave {player['name']}{colors['RESET']}                 ║")
    print(f"║   {colors['WHITE']}has survived the abyss...{colors['RESET']}              ║")
    print(f"║                                          ║")
    print(f"{colors['GREEN']}╚══════════════════════════════════════════╝{colors['RESET']}")
    time.sleep(2)

    os.system(o_system[0])
    print(f"\n{colors['WHITE']}>> Closing game session...{colors['RESET']}")
    time.sleep(1.5)
    os.system(o_system[0])


def lose():

    os.system(o_system[0])
    print(f"\n{colors['RED']}💀 Your vision fades into darkness...{colors['RESET']}")
    print(f"{colors['WHITE']} {player['name']} has fallen.{colors['RESET']}")
    time.sleep(2)

    os.system(o_system[0])
    print(f"\n{colors['RED']}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{colors['RESET']}")
    print(f"{colors['WHITE']}          🕯️  YOU DIED  🕯️          {colors['RESET']}")
    print(f"{colors['RED']}xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{colors['RESET']}")
    time.sleep(1.5)

    os.system(o_system[0])
    print(f"\n{colors['WHITE']}╔══════════════════════════════════════════╗{colors['RESET']}")
    print(f"║                                          ║")
    print(f"║   {colors['RED']}{enemy1['name']}{colors['WHITE']} was too strong...{colors['RESET']}        ║")
    print(f"║   {colors['WHITE']}Your soul remains in the terminal.     ║")
    print(f"║                                          ║")
    print(f"{colors['WHITE']}╚══════════════════════════════════════════╝{colors['RESET']}")
    time.sleep(2.5)

    os.system(o_system[0])
    print(f"\n{colors['RED']}>> Game Over. Better luck next time...{colors['RESET']}\n")
    time.sleep(1)
    os.system(o_system[0])