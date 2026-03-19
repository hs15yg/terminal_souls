BLACK = '\033[30m'
RED = '\033[31m'
RESET = '\033[0m'

# utilizo random para que me escoja un numero aleatorio dentro del rango
import random
#creo una funcion para saber el porcentaje del daño del heroe y el enemigo
def damage (min , max):
    #le he puesto de nombre a la funcion damage
    critical = random.randint(1 , 100)
    #utilizo la condicionales para que tome una decision dependiendo si es falsa o verdadera
    if critical >= 1 and critical <= 10:
        combat = random.randint(min , max)*2
    else:
        combat = random.randint(min , max)
    #utilizo return para devolver el daño realizado
    return combat

#funcion de barra de vida
def life_bar (hp, name):
    bar = ""   
    for i in range(1 , hp , 10):
        bar += "#"
    if name.lower() == "hero":
        return print(f"{name}: \nVida: {RED}{bar}{RESET}")
    else:
        return print(f"{name}: \nVida: {BLACK}{bar}{RESET}")

life_bar(120, "Hero")
