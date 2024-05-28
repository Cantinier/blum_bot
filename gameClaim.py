import random
import requests
import json
import auth_requests


def game_claim(gameId):
    url = "https://game-domain.blum.codes/api/v1/game/claim"
    token = auth_requests.get_token()
    points = random.randint(200, 300)
    payload = json.dumps({
      "gameId": f'{gameId}',
      "points": points
    })
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Accept-Encoding': 'gzip, deflate, br, zstd',
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {token}',
      'Origin': 'https://telegram.blum.codes',
      'Connection': 'keep-alive',
      'Referer': 'https://telegram.blum.codes/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(gameId + ' ' + response.text)

