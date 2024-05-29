import random
import time
import gameClaim
import play
from getBalance import get_balance


def play_game(count=0):
    available_count = get_balance()['playPasses']
    if available_count == 0:
        print('Нет повторов')
    else:
        if count == 0:
            count=available_count

        for _ in range(count):
            game_id = play.play()
            time.sleep(random.randint(30, 33))
            game_result = gameClaim.game_claim(game_id)
            current_balance = get_balance()['availableBalance']
            print(game_id + ' ' + game_result + ' | Баланс: '+current_balance)


play_game()
