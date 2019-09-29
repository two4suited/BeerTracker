import boto3

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from src.data.beertable import BeerTable


class BeersRepository:
    def __init__(self):
        client = boto3.resource("dynamodb")
        self.table = client.Table("Beers")

    def addbeer(self, beer):
        beeritem ={
            BeerTable.BeerName: beer.BeerName,
            BeerTable.BreweryName: beer.BreweryName,
            BeerTable.LocationName: beer.LocationName,
            BeerTable.Drank: beer.Drank,
            BeerTable.DateAdded: str(beer.DateAdded)
        }

        if beer.DrankWhen is not None:
            beeritem[BeerTable.DrankWhen]=str(beer.DrankWhen)

        if beer.LabelPath is not None:
            beeritem[BeerTable.LabelPath] = beer.LabelPath

        response = self.table.put_item(
            Item=beeritem
        )

    def getbeerbylocation(self, locationname):
        try:
            response = self.table.query(
                KeyConditionExpression=Key(BeerTable.LocationName).eq(locationname)
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Items"]
            return item

    def getbeer(self, beer):
        try:
            response = self.table.query(
                KeyConditionExpression=Key(BeerTable.LocationName).eq(beer.LocationName) & Key(BeerTable.BeerName).eq(beer.beerName)
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Items"]
            return item

    def update(self, beer):
        self.addbeer(beer)

    def delete(self, beer):
        self.table.delete_item(
            Key={
                BeerTable.LocationName: beer.LocationName,
                BeerTable.BeerName: beer.BeerName
            }
        )
