from scrap_oto import get_ids, get_urls, get_response
from parse_oto import parse_response
from database import create_flat

urls = get_urls(2)
print('URLs scraped...')
ids = get_ids(urls)
print('IDs acquired...')

for fi in ids:
    resp = get_response(fi)
    flat = parse_response(resp)
    create_flat(flat)
