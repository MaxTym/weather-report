import requests
import json
import os.path


class Astronomy:

    def get_weather(zip):
        filename = "astronomy_" + zip + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/astronomy/q/" + zip + ".json"
            r = requests.get(url)
            results = r.json()["moon_phase"]
            print("Sunrise: ", results["sunrise"], "Sunset: ", results["sunset"])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
        print("Sunrise: ", results["sunrise"], "Sunset: ", results["sunset"])
