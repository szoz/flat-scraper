from pymongo import MongoClient


def create_flat(collection, data):
    """Inserts given flat data into given DB collection.

    :param collection: MongoDB collection object.
    :param data: Data
    :return: None
    """
    collection.insert_one(data)


def read_all_flats(collection):
    """Reads all flats data in given DB collection."""
    return list(collection.find())


# def read_flat(collection, flat_id):
#     parameters = {'_id': flat_id}
#     return collection.find_one(parameters)

# def remove_flat(collection, flat_id):


def delete_flat(collection, flat_id):
    return collection.delete_one({'_id': flat_id})

client = MongoClient()
db = client['flat_base']
offers = db['offersoto']

flat1 = {
    "_id": 60232911,
    "url": "https://www.otodom.pl/oferta/dwupoziomowe-stan-deweloperski-praga-polnoc-ID44Jkz.html",
    "title": "Dwupoziomowe, Stan Deweloperski, Praga-P\u00f3\u0142noc.",
    "features": ["telewizja kablowa", "internet", "dwupoziomowe"],
    "date_created": {"2020-02-17T20:27:58": "2020-02-17 17:21:47"},
    "price": {"2020-02-17T20:27:58": "609000"},
    "address": "Warszawa, Praga-P\u00f3\u0142noc",
    "coordinates": "52.2608396+21.0599399",
    "characteristics": {
            "Powierzchnia": "63,50 m\u00b2",
            "Liczba pokoi": "3",
            "Rynek": "pierwotny",
            "Rodzaj zabudowy": "kamienica",
            "Pi\u0119tro": "4",
        },
    "photos": [
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImkwY2Y4ZW84N2FtOS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.dS6uW_H6nLGO4tQTQHVuzJIL3T_NDW_PqP8g1zQKSEU/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImkwY2Y4ZW84N2FtOS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.dS6uW_H6nLGO4tQTQHVuzJIL3T_NDW_PqP8g1zQKSEU/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imlvc3Zlam9kODF4aTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.2BzxKqKi4HZ2MMmOq2DiAdfKc6Lm7jLM5RvLigY_SCg/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imlvc3Zlam9kODF4aTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.2BzxKqKi4HZ2MMmOq2DiAdfKc6Lm7jLM5RvLigY_SCg/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imk0a3dyZXlqZTdnNi1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.LjR5WX8WELZvMa07gDcVEQO1v4tWqNp9NydvvinVvT0/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imk0a3dyZXlqZTdnNi1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.LjR5WX8WELZvMa07gDcVEQO1v4tWqNp9NydvvinVvT0/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6InQzNDB0NHQ0MnJ6MS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.gpVcP3Y9T5pIu2G1HxTc2GTlwnQCz9BdG72S1KxeNDI/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6InQzNDB0NHQ0MnJ6MS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.gpVcP3Y9T5pIu2G1HxTc2GTlwnQCz9BdG72S1KxeNDI/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjFxemUyOXk1Nm43MjMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vifgjIWgOQe4OhB67Mo4AfsIVRM9PGe6VJO_AABPIb8/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjFxemUyOXk1Nm43MjMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vifgjIWgOQe4OhB67Mo4AfsIVRM9PGe6VJO_AABPIb8/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Im56aXY1NTFkdjA4aDItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.t876fvRUgSGrmwVQ-4YUGTIH7lTfjcJm4Qa8SdBLkjo/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Im56aXY1NTFkdjA4aDItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.t876fvRUgSGrmwVQ-4YUGTIH7lTfjcJm4Qa8SdBLkjo/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRidHpyOWx5YXg0YTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.RdHuyNJgh5E-PV3qB7CIw4zfPFKi8d-R5ILlsVGdUgE/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRidHpyOWx5YXg0YTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.RdHuyNJgh5E-PV3qB7CIw4zfPFKi8d-R5ILlsVGdUgE/image;s=1280x1024;q=80"
        ]
    ]
}

flat2 = {
    "_id": 60211792,
    "url": "https://www.otodom.pl/oferta/nowe-bezposred-saska-kepa-3-pok-miedzynarodowa-ID44DPV.html",
    "title": "!NOWE! Bezpo\u015bred. Saska K\u0119pa 3 Pok. Mi\u0119dzynarodowa",
    "features": ["zmywarka", "lod\u00f3wka", "meble", "piekarnik", "pralka", "piwnica"],
    "date_created": {"2020-02-17T20:27:59": "2020-02-11 17:19:38"},
    "price": {"2020-02-17T20:27:59": "628000"},
    "address": "Warszawa, Praga-Po\u0142udnie, ul. Mi\u0119dzynarodowa",
    "coordinates": "52.23125509957763+21.067548157702632",
    "characteristics": {
        "Powierzchnia": "50 m\u00b2",
        "Rynek": "wt\u00f3rny",
        "Rodzaj zabudowy": "blok",
        "Pi\u0119tro": "3",
        "Liczba pi\u0119ter": "3",
    },
    "photos":
    [
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImU0MnFiNXdxcmI0dTMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.1S5tcONF7_7kcC9faQ2rV6RIz-QUIn_fsiUDI53QCJ4/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImU0MnFiNXdxcmI0dTMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.1S5tcONF7_7kcC9faQ2rV6RIz-QUIn_fsiUDI53QCJ4/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRueTNwd3o0b3ZwYjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.qYlq_QP5ijXx7tdxvG1UFPDT1d5dyC7P57Rej0a1AEo/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRueTNwd3o0b3ZwYjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.qYlq_QP5ijXx7tdxvG1UFPDT1d5dyC7P57Rej0a1AEo/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImdzaW94ODY2empyMTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vO2ah5nsfFwqjBpkU6zNYVSv9Gd9Fvl4bEfD1hw5Uq8/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImdzaW94ODY2empyMTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vO2ah5nsfFwqjBpkU6zNYVSv9Gd9Fvl4bEfD1hw5Uq8/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imt2Y3M2enZnbTNpODMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8tBJGAo86r0bwEWeBrBWQ0YVUH0eSBmNHD15GI43OQo/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imt2Y3M2enZnbTNpODMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8tBJGAo86r0bwEWeBrBWQ0YVUH0eSBmNHD15GI43OQo/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Inhnd2ExcWV3dTgwazItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.FzTqA2JUcLwb2-kFINhF8H6OPeQXmGnvGO3CEYOozZQ/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Inhnd2ExcWV3dTgwazItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.FzTqA2JUcLwb2-kFINhF8H6OPeQXmGnvGO3CEYOozZQ/image;s=1280x1024;q=80"
        ],
        [
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjVrbnI0Nmp5ZWVjbS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Fx0T74fotoF3_qMTzKCeSFf27q34sCtKfByU654DUV4/image;s=184x138;q=80",
            "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjVrbnI0Nmp5ZWVjbS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Fx0T74fotoF3_qMTzKCeSFf27q34sCtKfByU654DUV4/image;s=1280x1024;q=80"
        ]
    ]
}



if __name__ == '__main__':
    # print(read_all_flats(offers))
    print(delete_flat(offers, 60232911))
    print(delete_flat(offers, 60211792))
    create_flat(offers, flat1)
    create_flat(offers, flat2)
