"""Examples how creatio can be used to generate test data"""

from creatio.address.fi_FI import address
from creatio.name.fi_FI import name

print(address.home_address())
# Mäntykatu 10, 00280 Kokkola

print(name.full_name())
# Tapio Korhonen
