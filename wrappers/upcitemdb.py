import requests

class UPCItemDB:

    def __init__(self):
        self.base_url = 'https://api.upcitemdb.com/prod/trial'

    def get_item(self, barcode):
        url = self.base_url + '/lookup'

        headers = { 'Accept': 'application/json' }
        params = { 'upc': barcode }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            return None

        return response.json()