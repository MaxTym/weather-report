import requests
import json
import os.path


class Conditions:


    def get_weather(zip):
        print(zip)
        filename = "weather_" + zip + ".json"
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                results = results["current_observation"]
        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/conditions/q/" + zip + ".json"
            r = requests.get(url)
            results = r["current_observation"]
            print(results['display_location']['full'])
            print("temp: ", results['temp_c'], "C")
            print("temp: ", results['temp_f'], "F")
            print('humidity: ' , results['relative_humidity'])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
        print(results['display_location']['full'])
        print("temp: ", results['temp_c'], "C")
        print("temp: ", results['temp_f'], "F")
        print('humidity: ' , results['relative_humidity'])