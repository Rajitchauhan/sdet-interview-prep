"""DATA layer: products ka data ek jagah. Price/naam badla to sirf yahan badlo."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: float


BACKPACK = Product("backpack", "Backpack", 29.99)
BIKE_LIGHT = Product("bike-light", "Bike Light", 9.99)
ONESIE = Product("onesie", "Onesie", 7.99)

ALL_PRODUCTS = (BACKPACK, BIKE_LIGHT, ONESIE)
