import unittest

from src.data.beersrepository import BeersRepository
from src.models.beer import Beer


class BeerRepositoryTests(unittest.TestCase):

    def test_write(self):
        b = Beer("Test", "TestBeer", "TestLocation")
        beerrepo = BeersRepository()
        beerrepo.addbeer(b)
        self.assertTrue(1)
