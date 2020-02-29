from pymongo import MongoClient, DESCENDING

client = MongoClient()
db = client['flat_base']
collection = db['offersoto']


def create_flat(data):
    """Inserts given flat data into DB collection."""
    if collection.find_one({'_id': data['_id']}):
        return collection.update({'_id': data['_id']}, {"$push": {
            'scraped_date': data['scraped_date'][0], 'price': data['price'][0], 'price_pm': data['price_pm'][0],
            'added_date': data['added_date'][0], 'updated_date': data['updated_date'][0]
        }})
    return collection.insert_one(data)


def read_all_flats(limit=0, page=0, sort='updated'):
    """Reads all flats records from DB collection."""
    skip = limit * (page - 1)
    return collection.find(limit=limit, skip=skip).sort(f'{sort}_date', DESCENDING)


def get_flat_count():
    """Returns number of all flats in DB collection."""
    return collection.count()


def read_flat(flat_id):
    """Reads flat record with given ID."""
    parameters = {'_id': flat_id}
    return [collection.find_one(parameters)]


def delete_flat(flat_id):
    """Removes flat record wit given ID."""
    return collection.delete_one({'_id': flat_id})
