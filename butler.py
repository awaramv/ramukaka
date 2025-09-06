import schedule
# import time
import requests
import cleaner


def read_the_BKW_daily():
    try:
        response = requests.get("http://growattreader:5000/update_daily_data")
        if response.status_code == 200:
            cleaner.log_it("BKW-daily", "Success")
        else:
            cleaner.log_it("BKW-daily",
                           "Failure",
                           message=f"{response.reason}")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily", "Exception", Exception=e)


def read_the_BKW_aggregated():
    try:
        response = requests.get("http://growattreader:5000/update_aggregated_data")
        if response.status_code == 200:
            cleaner.log_it("BKW-agg", "Success")
        else:
            cleaner.log_it("BKW-agg",
                           "Failure",
                           message=f"{response.reason}")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily",
                       "Exception",
                       message="",
                       Exception=e)


def read_current_weather_data():
    try:
        response = requests.get("http://mausam:5000/save_weather_data/Hannover,DE")
        if response.status_code == 200:
            cleaner.log_it("Weather", "Success")
        else:
            print(f"Failed to read weather data, status code: {response.status_code}")
            cleaner.log_it("Weather", "Failure")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("Weather", "Exception", Exception=e)


schedule.every(1).hours.do(read_the_BKW_aggregated)
schedule.every(1).hours.do(read_the_BKW_daily)
schedule.every(15).minutes.do(read_current_weather_data)


cleaner.log_it("Pulse", "Initiate")
while True:
    schedule.run_pending()
