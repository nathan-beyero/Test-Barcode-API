import requests

class UPCItemDB:

    def __init__(self):
        self.base_url = 'https://api.upcitemdb.com/prod/trial'

    def get_product(self, barcode):
        url = self.base_url + '/lookup'

        headers = { 'Accept': 'application/json' }
        params = { 'upc': barcode }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            return None

        json = response.json()
        
        val = {
            "barcode_id": json['items'][0]['ean'],
            "name": json['items'][0]['title'],
            "description": json['items'][0]['description'],
            "category": json['items'][0]['category'].split(' > ')[-1]
        }

        return val