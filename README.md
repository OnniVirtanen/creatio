# Creatio

**Creatio** is a Python library designed to generate realistic test data for various purposes such as testing, development, and prototyping. It includes localized data generators for names, addresses, and more, with support for different regions and languages.

## Features
- Generate realistic names and addresses
- Support for localized data generation (e.g., Finnish data with `fi_FI`).
- Easy to use with simple function calls.
- Small number of dependencies, easy to audit!

## Installation
```bash
git clone https://github.com/OnniVirtanen/creatio.git
cd creatio
pip install . uv
```

## Usage
```python
from creatio.address.fi_FI import address
from creatio.name.fi_FI import name
from creatio.occupation.fi_FI import occupation

print(address.home_address())
# Example output: Mäntykatu 10, 00280 Kokkola

print(name.full_name())
# Example output: Tapio Korhonen

print(occupation.occupation())
# Example output: Tuotantotyöntekijä
```

## Supported locales
- Finnish (fi_FI)

## Unit testing
Run unit tests
```
uv run pytest
```