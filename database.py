from pymongo import MongoClient, DESCENDING
from pymongo.errors import DuplicateKeyError

client = MongoClient()
db = client['flat_base']
collection_oto = db['offersoto']
collection_gt = db['offersgt']


def create_flat(data, oto=True):
    """Inserts given flat data into DB collection."""
    if oto:
        if collection_oto.find_one({'_id': data['_id']}):
            return collection_oto.update({'_id': data['_id']}, {"$push": {
                'scraped_date': data['scraped_date'][0], 'price': data['price'][0], 'price_pm': data['price_pm'][0],
                'added_date': data['added_date'][0], 'updated_date': data['updated_date'][0]
            }})
        return collection_oto.insert_one(data)
    else:
        try:
            return collection_gt.insert_one(data)
        except DuplicateKeyError:
            return None


def read_all_flats(limit=0, page=0, sort='updated', oto=True):
    """Reads all flats records from DB collection."""
    skip = limit * (page - 1)
    if oto:
        return collection_oto.find(limit=limit, skip=skip).sort(f'{sort}_date', DESCENDING)
    else:
        return collection_gt.find(limit=limit, skip=skip).sort(f'{sort}_date', DESCENDING)


def get_flat_count(oto=True):
    """Returns number of all flats in DB collection."""
    return collection_oto.count() if oto else collection_gt.count()


def read_flat(flat_id, oto=True):
    """Reads flat record with given ID."""
    parameters = {'_id': flat_id}
    return [collection_oto.find_one(parameters)] if oto else [collection_gt.find_one(parameters)]


def delete_flat(flat_id, oto=True):
    """Removes flat record wit given ID."""
    return collection_oto.delete_one({'_id': flat_id}) if oto else collection_gt.delete_one({'_id': flat_id})
