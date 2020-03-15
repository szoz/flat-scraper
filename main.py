from tqdm import tqdm
from time import sleep

import scrap_oto as so
import parse_oto as po
import scrap_gt as sg
import parse_gt as pg
from database import create_flat

SEARCH_PAGES = 2


def process_oto():
    """Main function for otodom scraping and storing data in db."""
    urls = so.get_urls(SEARCH_PAGES)
    ids = so.get_ids(urls)

    for identifier in tqdm(ids, 'Record data scraping'):
        resp = so.get_response(identifier)
        flat = po.parse_response(resp)
        create_flat(flat)


def process_gt():
    """Main function for gumtree scraping and storing data in db."""
    urls = sg.get_urls(SEARCH_PAGES)
    for url in tqdm(urls, 'Record data scraping'):
        data = sg.get_html(url)
        try:
            details = pg.get_details(data)
            create_flat(details, oto=False)
        except TypeError:
            continue


if __name__ == '__main__':
    print('Processing Otodom:')
    sleep(0.1)
    process_oto()
    print('Processing Gumtree:')
    sleep(0.1)
    process_gt()
    input('Proccesing complete. Press enter to exit.')
