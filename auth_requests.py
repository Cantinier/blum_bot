import requests
import json

auth_query = ""

url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

payload = json.dumps({"query": auth_query})
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://telegram.blum.codes',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def get_auth(proxy=None):
    response = requests.post(url, headers=headers, data=payload, proxies=proxy)
    return response.json()

def read_token(proxy):
    try:
        with open("token", 'r', encoding='utf-8') as file:
            token = file.read().strip()
            if token:
                return token
            else:
                return refresh_token(proxy)
    except FileNotFoundError:
        return refresh_token(proxy)

def refresh_token(proxy):
    auth = get_auth(proxy)
    token = auth.get('token', {}).get('access')
    if token:
        with open('token', 'w', encoding='utf-8') as file:
            file.write(token)
    return token

def check_token(token, proxy):
    url = "https://game-domain.blum.codes/api/v1/user/balance"
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
    response = requests.get(url, headers=headers, proxies=proxy)
    return response

def get_token(proxy=None):
    token = read_token(proxy)
    response = check_token(token, proxy)
    if response.status_code == 401:
        token = refresh_token(proxy)
    return token

def get_proxy(user):
    pass

