from datetime import datetime


class Beer:
    def __init__(self, BreweryName, BeerName, LocationName, Drank, DrankWhen=None,LabelPath=None,DateAdded=datetime.utcnow()):
        self.BreweryName = BreweryName
        self.BeerName = BeerName
        self.LocationName = LocationName
        self.Drank = Drank
        self.DrankWhen = DrankWhen
        self.DateAdded = DateAdded
        self.UntappedId = None
        self.AlchoholByVolume = None
        self.Description = None
        self.LabelPath = LabelPath
        self.Style = None
        self.Ibu = None
        self.Rating = None

    def Drink(self):
        self.Drank = True
        self.DrankWhen = datetime.utcnow()
