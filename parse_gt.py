from datetime import date, datetime
from json import loads


def get_details(html):
    """Parses given HTML object scraped from gumtree flat offer page.

    :param html: HTML object from flat offer page.
    :return: Dict with parsed parameters.
    """
    try:
        details = {
            '_id': int(html.url.split('/')[-1][3:12]),
            'url': html.url,
            'price': int(html.find('.amount', first=True).full_text.split(u'\xa0')[0]) * 1000,
            'title': html.find('.myAdTitle', first=True).full_text.replace(u'\xa0', u' '),
            'scraped_date': date.today().isoformat(),
            'photos': [[ph.replace('/$_20', '/$_1'), ph.replace('/$_20', '/$_3')]
                       for ph in loads(html.find('.has-thumbs', first=True).full_text)['large']],
            'favorite': False
        }
    except AttributeError:
        return None

    chars = {char.find('.name', first=True).full_text: char.find('.value', first=True).full_text
             for char in html.find('.selMenu', first=True).find('.attribute')}

    m = int(chars.pop('Wielkość (m2)'))

    characteristics = {
        'm': f'{m} m²',
        'rooms_num': chars.pop('Liczba pokoi', ''),
        'building_type': chars.pop('Rodzaj nieruchomości', ''),
        'market': chars.pop('Na sprzedaż przez', '')
    }

    details['price_pm'] = details['price'] // m
    details['added_date'] = datetime.strptime(chars.pop('Data dodania'), '%d/%m/%Y').date().isoformat()
    details['address'] = chars.pop('Lokalizacja', '')

    details['characteristics'] = characteristics
    details['features'] = [f'{key} - {value}' for key, value in chars.items()]

    return details
