import boto3

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


class BeersRepository:
    def __init__(self):
        client = boto3.resource("dynamodb")
        self.table = client.Table("Beers")

    def addbeer(self, beer):
        response = self.table.put_item(
            Item={
                "BeerName": beer.BeerName,
                "BreweryName": beer.BreweryName,
                "LocationName": beer.LocationName,
                "Drank": beer.Drank
            }
        )

    def getbeerbylocation(self, locationname):
        try:
            response = self.table.query(
                KeyConditionExpression=Key("LocationName").eq(locationname)
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Items"]
            return item

    def getbeer(self, beer):
        try:
            response = self.table.query(
                KeyConditionExpression=Key("LocationName").eq(beer.LocationName) & Key("BeerName").eq(beer.beerName)
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Items"]
            return item

    def drink(self, beer):
        beer.Drank = True
        self.addbeer(beer)

    def delete(self, beer):
        self.table.delete_item(
            Key={
                "LocationName": beer.LocationName,
                "BeerName": beer.BeerName
            }
        )
