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
                "BeerName": beer.beerName,
                "BreweryName": beer.breweryName,
                "LocationName": beer.locationName
            }
        )

    def getbeerbylocation(self, locationname):
        try:
            response = self.table.get_item(
                Key={
                    "LocationName": locationname
                }
            )
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            item = response["Item"]
            return item


    def drink(self,locationname,beername):
        self.table.update_item(
            Key={
                "LocationName": locationname,
                "BeerName": beername
            },
            UpdateExpression="Set drank = :val1",
            ExpressionAttributesValues={
                ":val1": 1
            }
        )

    def delete(self,beer):
        self.table.delete_item(
            Key={
                "LocationName": beer.locationName,
                "BeerName": beer.beerName
            }
        )

