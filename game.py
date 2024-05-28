import random
import time
import gameClaim
import play
from getBalance import get_balance


def play_game(count=0):
    if count == 0:
        count = get_balance()['playPasses']
        if count == 0:
            print('Нет повторов')

    for _ in range(count):
        gameId = play.play()
        time.sleep(random.randint(30, 33))
        gameClaim.game_claim(gameId)


play_game()
