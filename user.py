import requests

class User:
    def __init__(self, ip):
        self.ip = ip
        self.country = self.get_country()

    def get_country(self):
        response = requests.get(f'https://ipinfo.io/{self.ip}/country')
        return response.text.strip()
