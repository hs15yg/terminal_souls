import headers

R = headers.colors["RED"]
W = headers.colors["WHITE"]
B = headers.colors["BLUE"]
Y = headers.colors["YELLOW"]
RS = headers.colors["RESET"]
G = headers.colors["GREEN"]

# i use random so it picks a random number within the range
import random
# i create a function to calculate the damage percentage of the hero and the enemy
def damage(life, malice = False, enemy = False):

    # i named the function damage
    critical = random.randint(1 , 100)
    # i use conditionals so it makes a decision depending on whether it is true or false
    if malice == True:
        combat = random.randint(30 , 50)
        if critical >= 1 and critical <= 10:
            combat = combat * 2
    elif enemy == True:
        combat = random(15, 20)
    else:
        combat = random.randint(10 , 25)
        if critical >= 1 and critical <= 10:
            combat = combat * 2
    # i use return to return the damage dealt
    
    life -= combat 
    print(f"You have dealt {combat} damage")  
    return life


# life bar function
def life_bar (hp_hero , hp_enemy , enemy, hero):
    if hp_enemy < 0:
        hp_enemy = 0
    if hp_hero < 0:
        hp_hero = 0
        
    hero_bar = ""   
    # use a for loop that goes from 1 to 100 (or 120 for the enemy) jumping by 10 this means the bar will be about 10 or 12 units long
    for i in range(1, 100 , 10):
        if i <= hp_hero:
            hero_bar += "#"
        else:
            hero_bar += "-"

    enemy_bar = "" 
    for i in range(1, 120 , 10):
        if i <= hp_enemy:
            enemy_bar += "#"
        else:
            enemy_bar += "-"
    # use variables like red ,reset and black. 
    bars = f"💪 {hero}: {G}{hero_bar}{RS} {hp_hero}% \n🦹 {enemy}: {R}{enemy_bar}{RS} {hp_enemy}%"
    return bars


def heal(character):
    if character:
        if headers.player["potions"] > 0:
            headers.player["hp"] += 20
            headers.player["potions"] -= 1
            return True
        else:
            return False
    
    if not character:
        if headers.enemy1["potions"] > 0:
            headers.enemy1["hp"] += 20
            headers.enemy1["potions"] -= 1
            return True
        else:
            return False