import boto3

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError


class BeersRepository:
    def __init__(self):
        self.client = boto3.dynamodb.client()

    def addbeer(self, beer):
        response = self.client.put_item(
            TableName="Beers",
            Item={
                "BeerName": beer.beerName,
                "BreweryName": beer.breweryName,
                "LocationName": beer.locationName
            }
        )

    def getbeerbylocation(self, locationname):
        try:
            response = self.client.get_item(
                Key={
                    "LocationName": locationname
                }
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Item"]
            return item
