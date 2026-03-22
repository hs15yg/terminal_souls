import os
import time
import headers
import life
import check

R = headers.colors["RED"]
W = headers.colors["WHITE"]
B = headers.colors["BLUE"]
Y = headers.colors["YELLOW"]
RS = headers.colors["RESET"]
G = headers.colors["GREEN"]

def player():
    interupt = True

    hero_hp = headers.player["hp"]
    enemy_hp = headers.enemy1["hp"]
    enemy_name = headers.enemy1["name"]
    hero_name = headers.player["name"]

    bars = life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name)       
    
    while interupt:
        os.system(headers.o_system[0]) 
        print(bars)
        
        menu = f"""
{W}┌──────────────────────────────┐
│        PLAYER TURN           │
└──────────────────────────────┘{RS}
 Options:

  1. {R}Attack ⚔️{RS}
  2. {W}Heal 💊{RS}
  3. {B}Special Ability ✨{RS}
  4. {Y}Dodge 💨{RS}
"""
        print(menu)
        
        try:    
            op = int(input(f" {W}Choice action -> {RS}"))
            
            if op == 1:
                os.system(headers.o_system[0])
                print(f"\n {R}>> Attacking enemy...{RS}")
                time.sleep(1)
                os.system(headers.o_system[0])
                headers.enemy1["hp"] = life.damage(enemy_hp)
                time.sleep(1)
                os.system(headers.o_system[0])
                hero_hp = headers.player["hp"]
                enemy_hp = headers.enemy1["hp"]
                print(life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name))
                interupt = False

            elif op == 2:
                os.system(headers.o_system[0])
                print(f"\n {W}>> Using Heal...{RS}")
                time.sleep(1)
                os.system(headers.o_system[0])
                if life.heal(True):
                    print(f"\n {G}++ HEALED! ++{RS}")
                    print(f" {W}You recovered {G}20 HP{W} 💊{RS}")
                    time.sleep(1)
                    check.player_hp()
                    interupt = False
                else:
                    print(f"\n {headers.colors['RED']}⚠️  EMPTY BOTTLE!{RS}")
                    print(f" {headers.colors['YELLOW']}You have no more potions in your inventory.{RS}")
                    time.sleep(1)

            elif op == 3:
                os.system(headers.o_system[0])
                print(f"\n {B}>> Casting special ability...{RS}")
                time.sleep(1)
                os.system(headers.o_system[0])
                headers.enemy1["hp"] = life.damage(enemy_hp, malice=True)
                time.sleep(1)
                os.system(headers.o_system[0])
                hero_hp = headers.player["hp"]
                enemy_hp = headers.enemy1["hp"]
                print(life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name))
                interupt = False

            elif op == 4:
                os.system(headers.o_system[0])
                print(f"\n {Y}>> Dodging attack...{RS}")
                time.sleep(1)
                interupt = False

            else:
                os.system(headers.o_system[0]) 
                print(f"\n{R} [x] INVALID OPTION {RS}")
                print(f"{Y} Please select a number from 1 to 4.{RS}")
                time.sleep(1)

        except:
            os.system(headers.o_system[0]) 
            print(f"\n{R} [x] INPUT ERROR {RS}")
            print(f"{Y} Check that you are entering numerical data!{RS}")
            time.sleep(1)

def enemy():

    hero_hp = headers.player["hp"]
    enemy_hp = headers.enemy1["hp"]
    enemy_name = headers.enemy1["name"]
    hero_name = headers.player["name"]

    os.system(headers.o_system[0])
    print(life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name))
    print(f"\n{R}┌──────────────────────────────┐")
    print(f"│      ⚠️  ENEMY TURN  ⚠️      │")
    print(f"└──────────────────────────────┘{RS}")
    time.sleep(1.2)


    if enemy_hp <= 24 and headers.enemy1["potions"] > 0:

        print(f"\n {enemy_name} looks wounded... He reaches for a potion! 🧪")
        time.sleep(1.5)
        
        life.heal(False) 
        
        os.system(headers.o_system[0])

        enemy_hp = headers.enemy1["hp"] 
        print(life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name))
        print(f"\n {G}>> {enemy_name} used a Potion! +20 HP ✨{RS}")
        time.sleep(2)

    else:
        print(f"\n {enemy_name} is preparing an attack...")
        time.sleep(1)

        os.system(headers.o_system[0])
        print(f"\n {R}>> {enemy_name} STRIKES! ⚔️{RS}")
        time.sleep(1)
        
        headers.player["hp"] = life.damage(hero_hp) 
        
        os.system(headers.o_system[0])
        hero_hp = headers.player["hp"]
        print(life.life_bar(hero_hp, enemy_hp, enemy_name, hero_name))
        print(f"\n {Y}>> Your HP has decreased!{RS}")
        time.sleep(2)