from urllib import response
import requests


def request_pln(data: dict):

    url = "URL/accuracy"
    try:
        requests.post(url=url, json=data)
    except Exception as erro:
        print("--------------------------------")
        print(erro)