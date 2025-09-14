"""Examples how creatio can be used to generate test data"""

from creatio.address.fi_FI import address
from creatio.name.fi_FI import name
from creatio.occupation.fi_FI import occupation

print(address.home_address())
# Mäntykatu 10, 00280 Kokkola

print(name.full_name())
# Tapio Korhonen

print(occupation.occupation())
# Tuotantotyöntekijä
