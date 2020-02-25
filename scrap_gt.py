"""
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
"""

from requests_html import HTMLSession
from urllib import parse
from itertools import product

# TODO shorten search_district values
def get_search_url(page=1):
    search_districts = {
        'mokotow': '/s-mieszkania-i-domy-sprzedam-i-kupie/mokotow/v1c9073l3200012p',
        'ochota': '/s-mieszkania-i-domy-sprzedam-i-kupie/ochota/v1c9073l3200013p',
        'praga_pld': '/s-mieszkania-i-domy-sprzedam-i-kupie/praga-poludnie/v1c9073l3200015p',
        'zoliborz': '/s-mieszkania-i-domy-sprzedam-i-kupie/zoliborz/v1c9073l3200026p',
        'wola': '/s-mieszkania-i-domy-sprzedam-i-kupie/wola/v1c9073l3200025p'
    }
    search_params = [
        {'nr': 2, 'pr': ',600000'},
        {'nr': 3, 'pr': ',600000'}
    ]

    return [f'https://www.gumtree.pl{district}{page}?{parse.urlencode(params)}'
            for district, params
            in product(search_districts.values(), search_params)]


def get_urls(pages):
    session = HTMLSession()

    urls = []
    for page in range(1, pages + 1):
        for url in get_search_url(page):
            r = session.get(url)
            urls.append(r.html.find('.view', first=True).absolute_links)

    return urls


def get_details(url):
    details = {'id': url.split('/')[-1][3:12]}
    session = HTMLSession()
    r = session.get(url)
    object = r.html.find('.selMenu', first=True)
    object2 = object.find('.attribute')
    object3 = {element.find('.name', first=True).full_text: element.find('.value', first=True).full_text for element in object2}
    details['rest'] = object3
    details['price'] = r.html.find('.amount', first=True).full_text
    return details


print(get_details('https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/3-pok-przy-galerii-mokotow-klucze-za-dwa-miesiace/1006968653520911486520009'))
print(get_details('https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mieszkanie-+-warszawa-mokotow-sluzew-blacharska/1006967949600911115501509'))
print(get_details('https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mieszkanie-warszawa-mokotow-54m2-nr-83091-3645-oms/1006969911090910535030709'))






"""
https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/3-pok-przy-galerii-mokotow-klucze-za-dwa-miesiace/1006968653520911486520009
1006968653520911486520009
...696865352

https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mieszkanie-+-warszawa-mokotow-sluzew-blacharska/1006967949600911115501509
1006967949600911115501509
   696794960
           v1u111155015p1

https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mieszkanie-warszawa-mokotow-54m2-nr-83091-3645-oms/1006969911090910535030709
1006969911090910535030709
...696991109
około 18:46

https://img.classistatic.com/crop/50x50/i.ebayimg.com/00/s/NDM0WDY5Mw==/z/di4AAOSwnw5eVSgE/$_14.JPG
                                        i.ebayimg.com/00/s/NDM0WDY5Mw==/z/di4AAOSwnw5eVSgE/$_20.JPG
"""
