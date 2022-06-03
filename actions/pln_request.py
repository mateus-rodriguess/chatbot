from urllib import response
import requests


def request_pln(data: dict):

    url_base = "http://api_pln:8090/accuracy"
   
    requests.post(url=url_base, json=data)
