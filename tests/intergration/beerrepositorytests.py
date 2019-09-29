import unittest

from src.data.beersrepository import BeersRepository
from src.models.beer import Beer



beer = Beer("Test", "TestBeer", "TestLocation",0)
beerrepo = BeersRepository()

print("Adding Beer")
beerrepo.addbeer(beer)
print("Successfully Added Beer")

print("Reading Beers in Location " + beer.locationName)
beerread = beerrepo.getbeerbylocation(beer.locationName)
print("Beername " + beerread["BeerName"])

print("Deleting Beer")
beerrepo.delete(beer)
print("Beer Deleted")


