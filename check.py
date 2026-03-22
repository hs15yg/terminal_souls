import headers
import os

def enemy_hp():

    if headers.enemy1["hp"] > 120:
        headers.enemy1["hp"] = 120  

    elif headers.enemy1["hp"] <= 0:
        return False
    
    else:
        return True

def player_hp():

    if headers.player["hp"] > 100:
        headers.player["hp"] = 100  

    elif headers.player["hp"] <= 0:
        return False
    
    else:
        return True

def win_or_lose():

    if headers.player["hp"] <= 0:
        return False
    
    if headers.enemy1["hp"] <= 0:
        return True


def o_system():

    o = os.system(headers.o_system[0])
    if o > 0:
        headers.o_system[0] = "cls"
