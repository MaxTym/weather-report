import requests
import json
import os.path


class Hurricane:

    def get_weather():
        filename = "hurricanes.json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                results = results["currenthurricane"]
                for i in results:
                    print(i["stormInfo"]["stormName_Nice"])
                    print(i["Current"]["Time"]["pretty"])
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/currenthurricane/view.json"
            r = requests.get(url)
            results = r.json()
            results = results["currenthurricane"]
            for i in results:
                print(i["stormInfo"]["stormName_Nice"])
                print(i["Current"]["Time"]["pretty"])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
