import requests
from datetime import date
import json


def parse_response(resp):
    """Parses given JSON from Otodom API response.

    :param resp: Dict from API response body.
    :return: Dict with parsed parameters.
    """
    filter_only = ['url', 'title', 'features', 'status']
    parsed_resp = {key: val for key, val in resp.items() if key in filter_only}

    parsed_resp['time_relevant'] = [
        [
            date.today().isoformat(),
            resp['price']['value'],
            resp['areaPrice']['value'],
            resp['dateCrated'],
            resp['dateModified']
        ]
    ]

    parsed_resp['_id'] = resp['id']
    parsed_resp['address'] = resp['addresses']['pl']
    parsed_resp['coordinates'] = f"{resp['coordinates']['latitude']}+{resp['coordinates']['longitude']}"
    parsed_resp['characteristics'] = {char['key']: char['value_translated'] for char in resp['characteristics']}
    parsed_resp['photos'] = [(photo['thumbnail'], photo['large']) for photo in resp['photos'].values()]

    return parsed_resp


if __name__ == '__main__':
    for url in ['https://www.otodom.pl/frontera/api/item/60232911', 'https://www.otodom.pl/frontera/api/item/60211792']:
        r = requests.get(url)
        j = r.json()
        print(json.dumps(parse_response(j)))

a = {
    "url": "https://www.otodom.pl/oferta/nowe-bezposred-saska-kepa-3-pok-miedzynarodowa-ID44DPV.html",
    "title": "!NOWE! Bezpo\u015bred. Saska K\u0119pa 3 Pok. Mi\u0119dzynarodowa",
    "features": ["zmywarka", "lod\u00f3wka", "meble", "piekarnik", "pralka", "piwnica"],
    "status": "active",
    "time_relevant": [
        ["2020-02-22T12", "2020-02-11 17:19:38", "2020-02-21 17:20:24", "628000", "12560"]
    ],
    "_id": 60211792,
    "address": "Warszawa, Praga-Po\u0142udnie, ul. Mi\u0119dzynarodowa",
    "coordinates": "52.23125509957763+21.067548157702632",
    "characteristics": {
        "m": "50 m\u00b2",
        "rooms_num": "3",
        "market": "wt\u00f3rny",
        "building_type": "blok",
        "floor_no": "3",
        "building_floors_num": "3",
        "building_material": "ceg\u0142a",
        "windows_type": "plastikowe",
        "heating": "miejskie",
        "construction_status": "do zamieszkania",
        "rent": "400 z\u0142"
    },
    "photos": [["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Ijk5dXh6c3phazV1NzItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.2xsQIBv544yppGse9gGlBpckUEd_0H9xvfUSeu3rk9k/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Ijk5dXh6c3phazV1NzItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.2xsQIBv544yppGse9gGlBpckUEd_0H9xvfUSeu3rk9k/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImtmNThpdWlsZnZibzMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.U3Op9VH_T955D_iSw8EUM1nvGvWKFVeD2A_cTsZGl34/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImtmNThpdWlsZnZibzMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.U3Op9VH_T955D_iSw8EUM1nvGvWKFVeD2A_cTsZGl34/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6InphMTE4YnJ6dTEzNjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.D3vnzpe2zeQtcOpnWVmsmlKR_rQrrp3sbGUxrtoi4zM/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6InphMTE4YnJ6dTEzNjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.D3vnzpe2zeQtcOpnWVmsmlKR_rQrrp3sbGUxrtoi4zM/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjF3dDBvemlwOGF2eC1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.u-Dvgh2GkmPvRll2l58ImpYvYoWBj2z6vnPi9dIcdEQ/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjF3dDBvemlwOGF2eC1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.u-Dvgh2GkmPvRll2l58ImpYvYoWBj2z6vnPi9dIcdEQ/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImU0MnFiNXdxcmI0dTMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.1S5tcONF7_7kcC9faQ2rV6RIz-QUIn_fsiUDI53QCJ4/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImU0MnFiNXdxcmI0dTMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.1S5tcONF7_7kcC9faQ2rV6RIz-QUIn_fsiUDI53QCJ4/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRueTNwd3o0b3ZwYjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.qYlq_QP5ijXx7tdxvG1UFPDT1d5dyC7P57Rej0a1AEo/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImRueTNwd3o0b3ZwYjItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.qYlq_QP5ijXx7tdxvG1UFPDT1d5dyC7P57Rej0a1AEo/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImdzaW94ODY2empyMTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vO2ah5nsfFwqjBpkU6zNYVSv9Gd9Fvl4bEfD1hw5Uq8/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImdzaW94ODY2empyMTEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.vO2ah5nsfFwqjBpkU6zNYVSv9Gd9Fvl4bEfD1hw5Uq8/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imt2Y3M2enZnbTNpODMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8tBJGAo86r0bwEWeBrBWQ0YVUH0eSBmNHD15GI43OQo/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Imt2Y3M2enZnbTNpODMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8tBJGAo86r0bwEWeBrBWQ0YVUH0eSBmNHD15GI43OQo/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Inhnd2ExcWV3dTgwazItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.FzTqA2JUcLwb2-kFINhF8H6OPeQXmGnvGO3CEYOozZQ/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6Inhnd2ExcWV3dTgwazItQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.FzTqA2JUcLwb2-kFINhF8H6OPeQXmGnvGO3CEYOozZQ/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjVrbnI0Nmp5ZWVjbS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Fx0T74fotoF3_qMTzKCeSFf27q34sCtKfByU654DUV4/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6IjVrbnI0Nmp5ZWVjbS1BUEwiLCJ3IjpbeyJmbiI6ImoxajNvMTNtNmJnbjEtQVBMIiwicyI6IjE0IiwicCI6IjEwLC0xMCIsImEiOiIwIn1dfQ.Fx0T74fotoF3_qMTzKCeSFf27q34sCtKfByU654DUV4/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImpibTJyY215cHcxajEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8h9j07wmcqjKwMA2RGBKaaGrqC9nvEukzeVZZOZaxrs/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImpibTJyY215cHcxajEtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.8h9j07wmcqjKwMA2RGBKaaGrqC9nvEukzeVZZOZaxrs/image;s=1280x1024;q=80"], ["https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImFqbHh0MHFqdGozdDMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.5EpXVKwXSCECTjxDPTG7smAmzQltNVT7mTl-ITtLtPU/image;s=184x138;q=80", "https://apollo-ireland.akamaized.net/v1/files/eyJmbiI6ImFqbHh0MHFqdGozdDMtQVBMIiwidyI6W3siZm4iOiJqMWozbzEzbTZiZ24xLUFQTCIsInMiOiIxNCIsInAiOiIxMCwtMTAiLCJhIjoiMCJ9XX0.5EpXVKwXSCECTjxDPTG7smAmzQltNVT7mTl-ITtLtPU/image;s=1280x1024;q=80"]]
}