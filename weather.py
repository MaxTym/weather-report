from conditions import Conditions
from forecast import Forecast
from astronomy import Astronomy
from alerts import Alerts
from hurricanes import Hurricane


def main():
    print("Welcome to weather report app")
    zip_code = input("Enter a zip code: ")
    choice = input("What would you like to search for?\n'1' -- weather conditions\n'2' -- 10 day forecast\n'3' -- Sunrise and sunset times\n'4' -- Current weather alerts\n'5' -- Hurricanes\n")
    if choice == '1':
        Conditions.get_weather(zip_code)
    if choice == '2':
        Forecast.get_weather(zip_code)
    if choice == '3':
        Astronomy.get_weather(zip_code)
    if choice == '4':
        Alerts.get_weather(zip_code)
    if choice == '5':
        Hurricane.get_weather()



if __name__ == "__main__":
    main()
