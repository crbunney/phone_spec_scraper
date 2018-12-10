#!/usr/bin/env python

from typing import List, Dict
import enum

# take list of phones
# get webpage for each phone
from bs4 import BeautifulSoup


class Field(enum.Enum):
    CHIPSET = 'chipset'

    def __str__(self):
        return self.value


def search_phone_urls(phone_names: List[str]) -> Dict[str, str]:
    return {}


def search_phone_url(phone_name: str) -> str:
    return ''


def get_phone_html(url: str) -> str:
    return ''


def parse_phone_html(html: str, fields: List[Field]) -> Dict[Field, str]:
    parser = BeautifulSoup(html, features='html.parser')
    val = parser.select('[data-spec="{}"]'.format(fields[0]))[0].get_text()
    return {fields[0]:val}

# search gsmarena for phone
# parse html for specs
# format specs and print to CSV
