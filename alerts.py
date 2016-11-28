import requests
import json
import os.path


class Alerts:

    def get_weather(zip):
        filename = "alerts_" + zip + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                results = results["alerts"]
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/alerts/q/" + zip + ".json"
            r = requests.get(url)
            results = r.json()
            print(results)
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
        print(results[0]["description"], results[0]["message"])
