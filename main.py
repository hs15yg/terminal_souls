import headers
import turns
import check


def init():
    
    game_over = headers.start()
    while game_over:

        if check.player_hp() and check.enemy_hp():
            turns.player()
            if check.enemy_hp():
                turns.enemy()
        else:
            if check.win_or_lose():
                headers.win()
                game_over = False
            else:
                headers.lose()
                game_over = False

check.o_system()
init()