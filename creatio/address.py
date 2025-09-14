"""Test data generator for Finnish addresses.

Provides functions to return random postal and home addresses.
"""

import random

STREETS = [
    "Mannerheimintie", "Aleksanterinkatu", "Esplanadi", "Hämeenkatu",
    "Satamakatu", "Kalevantie", "Lönnrotinkatu", "Pohjoisesplanadi",
    "Itäväylä", "Turuntie"
]

CITIES = [
    "Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu",
    "Turku", "Jyväskylä", "Lahti", "Kuopio", "Pori"
]

POSTAL_CODES = [
    "00100", "02100", "33100", "01300", "90100",
    "20100", "40100", "15100", "70100", "28100"
]

def kotiosoite() -> str:
    """Generate a full random address."""
    street = random.choice(STREETS)
    number = random.randint(1, 100)
    postal = random.choice(POSTAL_CODES)
    city = random.choice(CITIES)
    return f"{street} {number}, {postal} {city}"
