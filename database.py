from pymongo import MongoClient, DESCENDING
from pymongo.errors import DuplicateKeyError

client = MongoClient()
db = client['flat_base']
collection_oto = db['offersoto']
collection_gt = db['offersgt']


def create_flat(data, oto=True):
    """Inserts given flat offer data into otodom or gumtree DB collection.

    :param data: Dict with flat offer data.
    :param oto: Flag for choosing DB collection.
    :return: DB response for inserting new flat offer document.
    """
    if oto:
        if collection_oto.find_one({'_id': data['_id']}):
            return collection_oto.update(
                {'_id': data['_id']},
                {"$push": {'scraped_date': data['scraped_date'][0],
                           'price': data['price'][0],
                           'price_pm': data['price_pm'][0],
                           'added_date': data['added_date'][0],
                           'updated_date': data['updated_date'][0]}}
            )
        return collection_oto.insert_one(data)
    else:
        try:
            return collection_gt.insert_one(data)
        except DuplicateKeyError:
            return None


def read_all_flats(limit=0, page=0, sort='updated', oto=True):
    """Reads all flat offer records from otodom or gumtree DB collection.

    :param limit: Offer data per page limit.
    :param page: Offer data page number.
    :param sort: Sorting key.
    :param oto: Flag for choosing DB collection.
    :return: Sorted offers data list.
    """
    skip = limit * (page - 1)
    if oto:
        return collection_oto.find(limit=limit, skip=skip).sort(f'{sort}_date', DESCENDING)
    else:
        return collection_gt.find(limit=limit, skip=skip).sort(f'{sort}_date', DESCENDING)


def get_flat_count(oto=True):
    """Returns all flats offer number in otodom or gumtree DB collection.

    :param oto: Flag for choosing DB collection.
    :return: Flat offer number.
    """
    return collection_oto.count() if oto else collection_gt.count()


def read_flat(flat_id, oto=True):
    """ Returns offer data from otodom or gumtree DB collection based on given ID.

    :param flat_id: Flat offer ID.
    :param oto: Flag for choosing DB collection.
    :return: Flat offer data.
    """
    parameters = {'_id': flat_id}
    return [collection_oto.find_one(parameters)] if oto else [collection_gt.find_one(parameters)]


def delete_flat(flat_id, oto=True):
    """Removes offer data from  otodom or gumtree DB collection based on given ID.

    :param flat_id: Flat offer ID.
    :param oto: Flag for choosing DB collection.
    :return: DB response for deleting flat offer document.
    """
    return collection_oto.delete_one({'_id': flat_id}) if oto else collection_gt.delete_one({'_id': flat_id})
