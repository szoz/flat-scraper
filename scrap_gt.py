from requests_html import HTMLSession
from urllib import parse
from itertools import product


def get_search_url(page=1):
    """ Returns Gumtree search URLs.

    :param page: Search result page number.
    :return: Search URLs list.
    """
    search_districts = {
        'mokotow': 'mokotow/v1c9073l3200012p',
        'ochota': 'ochota/v1c9073l3200013p',
        'praga_pld': 'praga-poludnie/v1c9073l3200015p',
        'wola': 'wola/v1c9073l3200025p'
    }
    search_params = [
        {'nr': 2, 'pr': ',600000'},
        {'nr': 3, 'pr': ',600000'}
    ]

    return [f'https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/{district}{page}?{parse.urlencode(params)}'
            for district, params
            in product(search_districts.values(), search_params)]


def get_urls(pages):
    """Returns offer URLs from Gumtree based on given pages.

    :param pages: Search results pages.
    :return urls: Offer URLs list.
    """
    session = HTMLSession()

    urls = set()
    for page in range(1, pages + 1):
        for url in get_search_url(page):
            r = session.get(url)
            urls = urls.union(r.html.find('.view', first=True).absolute_links)

    return urls


def get_html(url):
    """Returns HTML object based on given Gumtree URL.

    :param url: Offer URL.
    :return:  Offer HTML object.
    """
    session = HTMLSession()

    r = session.get(url)
    return r.html
