import requests
import json
import os.path


class Forecast:


    def get_weather(zip):
        filename = "forecast_" + zip + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                results = results["txt_forecast"]["forecastday"]
        else:
            url = ("http://api.wunderground.com/api/dd53adf2370f476e/forecast10day/q/"
                    + zip + ".json")
            r = requests.get(url)
            results = r.json()["forecast"]
            print(results)
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
        for i in results:
            print(i["title"])
            print(i["fcttext_metric"])
            print("")
