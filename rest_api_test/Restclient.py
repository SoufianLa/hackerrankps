import http.client
import json


def post_():
    connection = http.client.HTTPSConnection('api.github.com')
    headers = {'Content-type': 'application/json'}
    foo = {'text': 'Hello world github/linguist#1 **cool**, and #1!'}
    json_foo = json.dumps(foo)
    connection.request('POST', '/markdown', json_foo, headers)
    response = connection.getresponse()
    print(response.read().decode())


def get_():
    connection = http.client.HTTPSConnection('demo5739179.mockable.io')
    headers = {'Content-type': 'application/json'}
    connection.request('GET', '/test', None, headers)
    response = connection.getresponse()
    res = response.read().decode()
    jsonResponse = json.loads(res)
    print(jsonResponse.get("msg"))


if __name__ == "__main__":
    get_()
