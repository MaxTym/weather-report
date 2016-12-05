import requests
import json
import os.path


class Conditions:


    def get_weather(zip):
        filename ='cache/weather_' + str(zip) + '.json'
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                results = json.loads(f.read())
                print(results['current_observation']['display_location']['full'])
                print("temp: ", results['current_observation']['temp_c'], "C")
                print("temp: ", results['current_observation']['temp_f'], "F")
                print('humidity: ' , results['current_observation']['relative_humidity'])

        else:
            url = "http://api.wunderground.com/api/dd53adf2370f476e/conditions/q/" + str(zip) + ".json"
            r = requests.get(url)
            results = r.json()
            print(results['current_observation']['display_location']['full'])
            print("temp: ", results['current_observation']['temp_c'], "C")
            print("temp: ", results['current_observation']['temp_f'], "F")
            print('humidity: ' , results['current_observation']['relative_humidity'])
            with open(filename, "w") as f:
                f.write(json.dumps(results, indent=4))
