from urllib import response
import requests


def request_pln(data: dict):

    url = "https://c21f-186-225-176-38.sa.ngrok.io/accuracy"
    try:
        requests.post(url=url, json=data)
    except Exception as erro:
        print("--------------------------------")
        print(erro)