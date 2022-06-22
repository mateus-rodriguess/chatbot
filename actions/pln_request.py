from urllib import response
import requests


def request_pln(data: dict):

    url = "https://6970-177-128-80-105.sa.ngrok.io/accuracy"
    try:
        requests.post(url=url, json=data)
    except Exception as error:
        pass
