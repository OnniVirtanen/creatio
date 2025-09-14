"""Datasets and methods for generating finnish occupations"""

import random

OCCUPATIONS = (
    "Lääkäri",
    "Tuotantotyöntekijä",
    "Ohjelmistokehittäjä",
    "Kirjanpitäjä",
    "Siivooja",
    "Sairaanhoitaja",
    "Lähihoitaja",
    "Rakennusinsinööri",
    "Myyjä",
    "Mekaanikko",
    "Levyseppähitsaaja",
    "Palomies",
    "Poliisi",
    "Putkimies",
    "Sähkömies",
    "Lakimies",
    "Rakennustyöntekijä",
)


def occupation() -> str:
    """Returns occupation"""
    return random.choice(OCCUPATIONS)
