import requests


class IP:
    @staticmethod
    def my_ip() -> str:
        return requests.get("https://api.ipify.org").text
