import unittest
import json

from src.data.beersrepository import BeersRepository
from src.models.beer import Beer
from src.helpers.dict2obj import Dict2Obj


beer = Beer("Test", "TestBeer", "TestLocation",False)
beerrepo = BeersRepository()

print("Adding Beer")
beerrepo.addbeer(beer)
print("Successfully Added Beer")

print("Reading Beers in Location " + beer.LocationName)
beers = beerrepo.getbeerbylocation(beer.LocationName)


for be in beers:
    b = Beer(**be)
    print(f"Beername {b.BeerName}")
    print(f"Beer Drank? {b.Drank}")
    print(f"Drink {b.BeerName}")
    beerrepo.drink(b)
    print(f"Beer Drank? {b.Drank}")

print("Deleting Beer")
beerrepo.delete(beer)
print("Beer Deleted")


