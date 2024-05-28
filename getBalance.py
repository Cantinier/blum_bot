import requests
from auth_requests import get_token


def get_balance():
    url = "https://game-domain.blum.codes/api/v1/user/balance"
    token = get_token()
    payload={}
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
      'authorization': f'Bearer {token}',
      'origin': 'https://telegram.blum.codes',
      'priority': 'u=1, i',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

print(get_balance())