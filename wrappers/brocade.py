import requests

class Brocade:

    def __init__(self):
        self.base_url = 'https://www.brocade.io/api/'

    def get_item(self, barcode):
        url = self.base_url + 'items/' + barcode

        headers = { 'Accept': 'application/json' }

        response = requests.get(url, params={}, headers=headers)

        if response.status_code != 200:
            return None

        return response.json()