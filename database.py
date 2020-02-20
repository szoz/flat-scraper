from pymongo import MongoClient

client = MongoClient()
db = client['flat_base']
collection = db['offersoto']


def create_flat(data):
    """Inserts given flat data into DB collection."""
    return collection.insert_one(data)


def read_all_flats(limit=0, page=0):
    """Reads all flats records from DB collection."""
    skip = limit * (page - 1)
    return list(collection.find(limit=limit, skip=skip))


def read_flat(flat_id):
    """Reads flat record with given ID."""
    parameters = {'_id': flat_id}
    return [collection.find_one(parameters)]


def delete_flat(flat_id):
    """Removes flat record wit given ID."""
    return collection.delete_one({'_id': flat_id})
