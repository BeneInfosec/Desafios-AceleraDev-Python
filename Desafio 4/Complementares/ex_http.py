import requests

#Token
token_url = 'https://httpbin.org/bearer'

token = 'Bearer MySuperToken' #POde mudar o MySuperToken por um hash

response =  requests.get(token_url, headers ={'Authorization': token})
print(f'Token Status Code: {response.status_code}')
print(f'Token Response: {response.json()}')

#Cookies
cookies_jar = {
    'session_id': '123456bcd',
    'last_visited': '2019-09-09'
}

set_cookie_url = 'https://httpbin.org/cookies/set/{}/{}' #Primeiro argumento = NomeCookie / Segundo argumento = ConteudoCookie
cookies_url = 'https://httpbin.org/cookies'

print('\n=================================================================\n')
with requests.session() as session:
    for cookie in cookies_jar:
        session.get(set_cookie_url.format(cookie, cookies_jar[cookie]))

    response = session.get(cookies_url)
    print(response.json())
