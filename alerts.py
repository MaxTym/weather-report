import requests
import json
import os.path


class Alerts:

    def get_weather(zip):
        filename = "cache/alerts_" + str(zip) + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                results = results["alerts"]
                print(results[0]["description"], results[0]["message"])
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/alerts/q/" + str(zip) + ".json"
            r = requests.get(url)
            results = r.json()
            results = results["alerts"]
            print(results[0]["description"], results[0]["message"])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
