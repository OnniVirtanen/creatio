"""Test data generator for Finnish names.

Provides random Finnish first names, last names, and full names
using internal sets of common names.
"""

import random

FIRST_NAMES = {
    "Aino", "Eero", "Liisa", "Mikko", "Sanna",
    "Juho", "Helmi", "Oskari", "Kaisa", "Ville"
}

LAST_NAMES = {
    "Virtanen", "Korhonen", "Nieminen", "Mäkinen", "Hämäläinen",
    "Laine", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen"
}

def first_name() -> str:
    """Return a random first name from the internal dataset."""
    return random.choice(list(FIRST_NAMES))

def last_name() -> str:
    """Return a random last name from the internal dataset."""
    return random.choice(list(LAST_NAMES))

def full_name() -> str:
    """Return a randomly generated full name."""
    return f"{first_name()} {last_name()}"
