BLACK = '\033[30m'
RED = '\033[31m'
RESET = '\033[0m'

# i use random so it picks a random number within the range
import random
# i create a function to calculate the damage percentage of the hero and the enemy
def damage(life, min=10, max=25, malice = False):

    # i named the function damage
    critical = random.randint(1 , 100)
    # i use conditionals so it makes a decision depending on whether it is true or false
    if critical >= 1 and critical <= 10 and malice == True:
        combat = random.randint(30 , 50)*2
    else:
        combat = random.randint(min , max)
    # i use return to return the damage dealt
    
    life -= combat
    
    return print("the hero has lost this part of life 😢" , combat )


# life bar function
def life_bar (hp_hero , hp_enemy , enemy, hero):
    hero_bar = ""   
    for i in range(1, hp_hero , 10):
        hero_bar += "#"

    enemy_bar = "" 
    for i in range (1, hp_enemy , 10):
        enemy_bar += "#"

    return print(f"💪{hero}: {RED}{hero_bar}{RESET} {hp_hero}% \n🦹{enemy}: {BLACK}{enemy_bar}{RESET} {hp_enemy}%")
    



life_bar (100, 120, "enemy","hero")

damage(life=100)

