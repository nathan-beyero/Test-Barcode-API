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
        
        # need to make sure these 2 fields are not empty
        image = json['items'][0]['images']
        category = json['items'][0]['category']
        
        val = {
            "barcode": json['items'][0]['ean'],
            "name": json['items'][0]['title'].lower(),
            "description": json['items'][0]['description'].lower(),
            "brand": json['items'][0]['brand'].lower(),
            "image": image[0] if image else "",
            "category": category.split('>')[-1].strip().lower() if category else "",
        }

        return val