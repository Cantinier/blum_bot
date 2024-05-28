import requests

import auth_requests


def play():
    url = "https://game-domain.blum.codes/api/v1/game/play"
    token = auth_requests.get_token()
    payload={}
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Accept-Encoding': 'gzip, deflate, br, zstd',
      'Authorization': f'Bearer {token}',
      'Origin': 'https://telegram.blum.codes',
      'Connection': 'keep-alive',
      'Referer': 'https://telegram.blum.codes/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache',
      'Content-Length': '0',
      'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    gameId = response.json()['gameId']
    return gameId
