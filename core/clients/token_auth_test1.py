import requests

from pprint import  pprint
#'key': '87a97b2afe11aa13c81b413285a8c9e93f316e38'
def client():
    credentials = {
        'username': 'testinguser',
        'password': '123456Test'
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials
    )

    print('Status Code:', response.status_code)
    response_data =  response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()