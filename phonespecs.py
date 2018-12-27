#!/usr/bin/env python

from typing import List, Dict
import enum

# take list of phones
# get webpage for each phone
import requests
from bs4 import BeautifulSoup


class Field(enum.Enum):
    BATTERY_TECH = 'battype-hl'
    BATTERY_SIZE = 'batsize-hl'
    # CARD_SLOT = ''  # contained in storage text
    CHIPSET = 'chipset'
    CAMERA_FRONT = 'cam2modules'
    CAMERA_MAIN = 'camerapixels-hl'
    MODEL = 'modelname'
    PRICE = 'price'
    RAM = 'ramsize-hl'
    RELEASED = 'released-hl'
    RESOLUTION = 'displayres-hl'
    SIZE = 'displaysize-hl'
    STORAGE = 'storage-hl'

    # URL = ''  # use canonical from <head>

    def __str__(self):
        return self.value

    def __repr__(self):
        return 'Field.' + self.name


def search_phone_urls(phone_names: List[str]) -> Dict[str, str]:
    return {}


def search_phone_url(phone_name: str) -> str:
    return ''


def get_phone_html(url: str) -> str:
    return requests.get(url).content


def parse_phone_html(html: str, fields: List[Field]) -> Dict[Field, str]:
    parser = BeautifulSoup(html, features='html.parser')
    results = {}
    for field in fields:
        results[field] = parser.select('[data-spec="{}"]'.format(field))[0].get_text()

    # cleanup results
    if Field.CAMERA_FRONT in results:
        results[Field.CAMERA_FRONT] = results[Field.CAMERA_FRONT].split(' ')[0]
    if Field.PRICE in results:
        price = results[Field.PRICE].split(' ')
        results[Field.PRICE] = '~{}{}'.format(SYMBOLS[price[2]], price[1])
    return results


SYMBOLS = {
    'EUR': '€',
    'GBP': '£',
    'USD': '$',
}


def export_csv(rows: List[Dict[Field, str]], sep='\t'):
    field_order = [
        Field.MODEL, Field.PRICE, Field.RELEASED, Field.SIZE, Field.RESOLUTION, Field.CHIPSET, Field.RAM,
        Field.CAMERA_MAIN, Field.CAMERA_FRONT, Field.BATTERY_TECH, Field.BATTERY_SIZE, Field.STORAGE,
        # Field.CARD_SLOT, Field.URL
    ]
    # Print headings
    print(sep.join(f.name for f in field_order))

    # Print rows
    for row in sorted(rows, key=lambda r: r[Field.MODEL]):
        print(sep.join(row[f] for f in field_order))


# search gsmarena for phone
# parse html for specs
# format specs and print to CSV
PHONES = [
    'https://www.gsmarena.com/apple_iphone_6s-7242.php',
    'https://www.gsmarena.com/apple_iphone_x-8858.php',
    'https://www.gsmarena.com/lg_nexus_5-5705.php',
    'https://www.gsmarena.com/google_pixel-8346.php',
    'https://www.gsmarena.com/google_pixel_2-8733.php',
    'https://www.gsmarena.com/google_pixel_3-9256.php',
    'https://www.gsmarena.com/lg_g7_one-9304.php',
    'https://www.gsmarena.com/lg_g7_fit-9305.php',
    'https://www.gsmarena.com/lg_g7_thinq-9115.php',
    'https://www.gsmarena.com/nokia_8_1_(nokia_x7)-9342.php',
    'https://www.gsmarena.com/samsung_galaxy_j5-7184.php',
    'https://www.gsmarena.com/samsung_galaxy_s7-7821.php',
    'https://www.gsmarena.com/samsung_galaxy_s9-8966.php',

]


def do_main():
    results = []
    for p in PHONES:
        results.append(parse_phone_html(get_phone_html(p), list(Field)))
    export_csv(results)


if __name__ == '__main__':
    do_main()
