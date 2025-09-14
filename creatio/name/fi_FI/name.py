"""Datasets and methods for generating finnish names"""

import random

FIRSTNAMES_MALE = (
    "Juhani",
    "Johannes",
    "Olavi",
    "Antero",
    "Tapani",
    "Kalevi",
    "Tapio",
    "Matti",
    "Mikael",
    "Ilmari",
)

FIRSTNAMES_WOMEN = (
    "Maria",
    "Helena",
    "Johanna",
    "Anneli",
    "Kaarina",
    "Anna",
    "Marjatta",
    "Liisa",
    "Sofia",
    "Annikki",
)

LASTNAMES = (
    "Korhonen",
    "Virtanen",
    "Mäkinen",
    "Nieminen",
    "Mäkelä",
    "Laine",
    "Hämäläinen",
    "Heikkinen",
    "Koskinen",
    "Järvinen",
)


def firstname_gender(is_male: bool) -> str:
    """Returns firstname by gender"""
    if is_male:
        return random.choice(FIRSTNAMES_MALE)

    return random.choice(FIRSTNAMES_WOMEN)


def firstname() -> str:
    """Returns firstname"""
    return firstname_gender(random.random() < 0.5)


def lastname() -> str:
    """Returns lastname"""
    return random.choice(LASTNAMES)


def full_name() -> str:
    """Returns first and lastname concatenated"""
    return firstname() + " " + lastname()
