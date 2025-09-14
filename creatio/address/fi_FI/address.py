"""Datasets and methods for generating finnish addresses"""

import string
import random

POSTCODES = (
    "00100",
    "00120",
    "00130",
    "00140",
    "00150",
    "00170",
    "00180",
    "00200",
    "00220",
    "00230",
    "00250",
    "00260",
    "00270",
    "00280",
    "00300",
    "00320",
    "00330",
    "00340",
    "00350",
    "00400",
    "00410",
    "00420",
    "00430",
    "00500",
    "00510",
    "00520",
    "00530",
    "00550",
    "00580",
    "00600",
    "00610",
    "00620",
    "00630",
    "00800",
    "00810",
    "00820",
    "00830",
    "00840",
    "00850",
    "00900",
    "00910",
    "00920",
    "00930",
    "00940",
    "00950",
    "01100",
    "01200",
    "01300",
    "01400",
    "01500",
    "01600",
    "01700",
    "01800",
    "01900",
    "02100",
    "02200",
    "02300",
    "02400",
    "02500",
    "02600",
    "02700",
    "02800",
    "02900",
    "04100",
    "04200",
    "04300",
    "04400",
    "04500",
    "04600",
    "04700",
    "04800",
    "04900",
    "06100",
    "06200",
    "06300",
    "06400",
    "06500",
    "06600",
    "06700",
    "06800",
    "06900",
    "07100",
    "07200",
    "07300",
    "07500",
    "07600",
    "07700",
    "07800",
    "08100",
    "08200",
    "08300",
    "08400",
    "08500",
    "08600",
    "08700",
    "09100",
    "09200",
    "09300",
    "09400",
    "09500",
)

CITIES = (
    "Helsinki",
    "Espoo",
    "Vantaa",
    "Tampere",
    "Turku",
    "Oulu",
    "Jyväskylä",
    "Lahti",
    "Kuopio",
    "Pori",
    "Lappeenranta",
    "Kotka",
    "Joensuu",
    "Rovaniemi",
    "Seinäjoki",
    "Kokkola",
    "Vaasa",
    "Mikkeli",
    "Savonlinna",
    "Kajaani",
    "Hyvinkää",
    "Salo",
    "Rauma",
    "Lohja",
    "Kemi",
    "Nurmijärvi",
    "Kemijärvi",
    "Pieksämäki",
    "Inari",
    "Naantali",
)

STREET_PREFIXES = (
    "Mustikka",
    "Vanha",
    "Uusi",
    "Tieto",
    "Mattilan",
    "Mikkolan",
    "Laurilan",
    "Mänty",
)

STREET_POSTFIXES = ("kuja", "katu", "tie")

HOUSE_NUMBER = tuple(str(i) for i in range(1, 20))

HOUSE_CHARACTER = tuple(string.ascii_uppercase[:9])

APARTMENT_NUMBER = tuple(str(i) for i in range(1, 30))


def street_address() -> str:
    """Returns street address"""
    result = (
        random.choice(STREET_PREFIXES)
        + random.choice(STREET_POSTFIXES)
        + " "
        + random.choice(HOUSE_NUMBER)
    )

    if random.random() < 0.4:
        result += (
            " " + random.choice(HOUSE_CHARACTER) + " " + random.choice(APARTMENT_NUMBER)
        )

    return result


def postcode() -> str:
    """Returns postal code"""
    return random.choice(POSTCODES)


def city() -> str:
    """Returns city"""
    return random.choice(CITIES)


def home_address() -> str:
    """Returns home address"""
    return street_address() + ", " + postcode() + " " + city()
