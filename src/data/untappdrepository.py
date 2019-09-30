import os
import requests

class UntappdRepository:
    def __init__(self):
        self._url="https://api.untappd.com/v4/"
        self._clientId = os.environ.get("UNTAPPD_CLIENTID")
        self._clientKey = os.environ.get("UNTAPPD_CLIENTSECRET")

    def beersearch(self,beername):
        beersearchpath = "search/beer"

        response = requests.get(
            f"{self._url}{beersearchpath}?client_id={self._clientId}&client_secret={self._clientKey}&q={beername}")

        print(response.status_code)

        beersearch = response.json()

        #for beer in beersearch["response"]["beers"]["items"]:
         #   print(beer["beer"]["beer_name"])


