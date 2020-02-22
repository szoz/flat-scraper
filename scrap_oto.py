from requests_html import HTMLSession
import requests
from urllib import parse
import re


def get_search_url(page=None, **kwargs):
    """Returns Otodom search URL.

    :param page: Search result page number.
    :param kwargs: Additional query strings params.
    :return: Search URL.
    """
    search_districts = {
        'mokotow': 39,
        'ochota': 40,
        'praga_pld': 41,
        'zoliborz': 53,
        'wola': 117
    }
    search_params = {
        'search[filter_float_m:from]': 40,
        'search[filter_float_m:to]': 60,
        'search[filter_enum_rooms_num][0]': 2,
        'search[filter_enum_rooms_num][1]': 3,
        'search[filter_float_build_year:from]': 2000,
        'search[filter_float_build_year:to]': 2019,
        'search[filter_float_price:to]': 600000,
        'search[description]': 1,
        'nrAdsPerPage': 72,
    }

    for index, district in enumerate(search_districts.values()):
        search_params[f'locations[{index}][region_id]'] = 7
        search_params[f'locations[{index}][subregion_id]'] = 197
        search_params[f'locations[{index}][city_id]'] = 26
        search_params[f'locations[{index}][district_id]'] = district
    if page:
        search_params['page'] = page
    search_params.update(kwargs)

    return f'https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?{parse.urlencode(search_params)}'


def get_urls(pages):
    """Returns offer URLs from Otodom based on given pages

    :param pages: Search results pages.
    :return urls: Offer URLs list.
    """
    session = HTMLSession()

    urls = []
    for page in range(1, pages + 1):
        r = session.get(get_search_url(page))
        for url in r.html.links:
            if 'oferta' in url:
                urls.append(url)

    return urls


def get_ids(urls):
    """Returns offer identifiers based on give urls.

    :param urls: Offer URLs list.
    :return identifiers: Offer identifiers list.
    """
    session = HTMLSession()

    id_pattern = re.compile(r'\s\d{8}\s')
    identifiers = []
    for url in urls:
        r = session.get(url)
        title = r.html.find('title', first=True).text
        id_num = re.search(id_pattern, title).group(0)[1:-1]
        identifiers.append(id_num)
    return identifiers


def get_response(identifier):
    r = requests.get(f'https://www.otodom.pl/frontera/api/item/{identifier}')
    return r.json()


if __name__ == '__main__':
    print(get_ids(get_urls(pages=2)))
