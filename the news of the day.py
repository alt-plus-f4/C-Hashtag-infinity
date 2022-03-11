import requests
import datetime

nasa_api_key = "8DfEhspAfjMGPWckNEJqr81Zrfv4mqBgMXCSrFDa"

r = requests.get("https://api.nasa.gov/planetary/apod?api_key=8DfEhspAfjMGPWckNEJqr81Zrfv4mqBgMXCSrFDa")

print(r.content)

class NasaApi:
    def __init__(self, api_key):
        self.api_key = api_key

    def daily_content(self):
        _link = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}"
        return requests.get(_link)

    def asteroids(self):
        _link = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={datetime.date.today() - datetime.timedelta(days=7)}&api_key={self.api_key}"


api_test = NasaApi(nasa_api_key)

print(api_test.daily_content())
print(datetime.date.today() - datetime.timedelta(days=7))

