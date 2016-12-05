import requests
import json
import os.path


class Astronomy:

    def get_weather(zip):
        filename = 'cache/astronomy_' + str(zip) + '.json'
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                print("Sunrise: ", results["sunrise"], "Sunset: ", results["sunset"])
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/astronomy/q/" + str(zip) + ".json"
            r = requests.get(url)
            results = r.json()["moon_phase"]
            print("Sunrise: ", results["sunrise"], "Sunset: ", results["sunset"])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
