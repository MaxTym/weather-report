from conditions import Conditions
from forecast import Forecast
from astronomy import Astronomy
from alerts import Alerts
from hurricanes import Hurricane


def get_zip_code():
    while True:
        zip_code = input("Enter a zip code: ")
        try:
            zip_code = int(zip_code)
        except ValueError:
            print("Please enter a valid zip code")
        if len(str(zip_code)) != 5:
            print("Please enter a valid zip code")
        else:
            return zip_code
            break


def get_users_choice(zip_code):
    choice = input("What would you like to search for?\n'1' -- weather conditions\n'2' -- 10 day forecast\n'3' -- Sunrise and sunset times\n'4' -- Current weather alerts\n'5' -- Hurricanes\n")
    if choice == '1':
        try:
            Conditions.get_weather(zip_code)
        except:
            print("No cities match your zip code")
            main()
    if choice == '2':
        try:
            Forecast.get_weather(zip_code)
        except:
            print("No cities match your zip code")
            main()
    if choice == '3':
        try:
            Astronomy.get_weather(zip_code)
        except:
            print("No cities match your zip code")
            main()
    if choice == '4':
        try:
            Alerts.get_weather(zip_code)
        except:
            print("No cities match your zip code")
            main()
    if choice == '5':
        try:
            Hurricane.get_weather()
        except:
            print("No cities match your zip code")
            main()


def main():
    print("Welcome to weather report app")
    zip_code = get_zip_code()
    get_users_choice(zip_code)


if __name__ == "__main__":
    main()
