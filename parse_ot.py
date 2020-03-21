import requests
from datetime import date
import json


def parse_response(resp):
    """Parses given JSON from Otodom API response.

    :param resp: Dict from API response body.
    :return: Dict with parsed parameters.
    """
    filter_only = ['url', 'title', 'features', 'status']
    parsed_resp = {key: val for key, val in resp.items() if key in filter_only}

    parsed_resp['scraped_date'] = [date.today().isoformat()]
    parsed_resp['price'] = [resp['price']['value']]
    parsed_resp['price_pm'] = [resp['areaPrice']['value']]
    parsed_resp['added_date'] = [resp['dateCrated']]
    parsed_resp['updated_date'] = [resp['dateModified']]

    parsed_resp['_id'] = resp['id']
    parsed_resp['address'] = resp['addresses']['pl']
    parsed_resp['coordinates'] = f"{resp['coordinates']['latitude']}+{resp['coordinates']['longitude']}"
    parsed_resp['characteristics'] = {char['key']: char['value_translated'] for char in resp['characteristics']}
    parsed_resp['photos'] = [(photo['thumbnail'], photo['large']) for photo in resp['photos'].values()]

    return parsed_resp


if __name__ == '__main__':
    for url in ['https://www.otodom.pl/frontera/api/item/60232911', 'https://www.otodom.pl/frontera/api/item/60211792']:
        r = requests.get(url)
        j = r.json()
        print(json.dumps(parse_response(j)))
