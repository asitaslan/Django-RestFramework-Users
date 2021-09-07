import requests

from pprint import  pprint
#'key': '87a97b2afe11aa13c81b413285a8c9e93f316e38'
def client():
    token = 'Token 87a97b2afe11aa13c81b413285a8c9e93f316e38'
    headers = {
        'Authorization': token,
    }
    response = requests.get(
        url = 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers = headers,
    )

    print('Status Code:', response.status_code)
    response_data =  response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()