from datetime import date, datetime
from json import loads
from pprint import pprint

from scrap_gt import get_html


def get_details(html):
    try:
        details = {
            '_id': int(html.url.split('/')[-1][3:12]),
            'url': html.url,
            'price': int(html.find('.amount', first=True).full_text.split(u'\xa0')[0]) * 1000,
            'title': html.find('.myAdTitle', first=True).full_text.replace(u'\xa0', u' '),
            'scraped_date': date.today().isoformat(),
            'photos': [[ph.replace('/$_20', '/$_0'), ph.replace('/$_20', '/$_3')]
                       for ph in loads(html.find('.has-thumbs', first=True).full_text)['large']]
        }
    except AttributeError:
        return None

    chars = {char.find('.name', first=True).full_text: char.find('.value', first=True).full_text
             for char in html.find('.selMenu', first=True).find('.attribute')}

    m = int(chars.pop('Wielkość (m2)'))

    characteristics = {
        'm': f'{m} m²',
        'rooms_num': chars.pop('Liczba pokoi', '') ,
        'building_type': chars.pop('Rodzaj nieruchomości', ''),
        'market': chars.pop('Na sprzedaż przez', '')
    }

    details['price_pm'] = details['price'] // m
    details['added_date'] = datetime.strptime(chars.pop('Data dodania'), '%d/%m/%Y')\
        .date().isoformat()
    details['address'] = chars.pop('Lokalizacja', '')

    details['characteristics'] = characteristics
    details['features'] = [f'{key} - {value}' for key, value in chars.items()]

    return details


if __name__ == '__main__':
    url1 = 'https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/mokotow/mokotow-2-pokoje-pow-44-m2-ekskluzywna' \
           '-oferta/1007041428710912407250109'
    url2 = 'https://www.gumtree.pl/a-mieszkania-i-domy-sprzedam-i-kupie/wola/mieszkanie-warszawa-wola-46m2-nr-482148/' \
           '1007042176420912099690009'

    pprint(get_details(get_html(url1)))
    pprint(get_details(get_html(url2)))

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
