import requests
import json
import os.path


class Forecast:


    def get_weather(zip):
        filename = "cache/forecast_" + str(zip) + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                for i in results:
                    print(i["title"])
                    print(i["fcttext_metric"])
                    print("")
        else:
            url = ("http://api.wunderground.com/api/dd53adf2370f476e/forecast10day/q/" + str(zip) + ".json")
            r = requests.get(url)
            results = r.json()
            results = results['forecast']['txt_forecast']['forecastday']
            for i in results:
                print(i["title"])
                print(i["fcttext_metric"])
                print("")
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
