import schedule
import time
import requests
import cleaner


def read_the_BKW_daily():
    try:
        response = requests.get("http://growattreader:5000/update_daily_data")
        if response.status_code == 200:
            cleaner.log_it("BKW-daily", "Success")
            cleaner.sync_BKW_data_with_drive("BKW-daily")

        else:
            cleaner.log_it("BKW-daily", "Failure")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily", "Exception", Exception=e)


def read_the_BKW_aggregated():
    try:
        response = requests.get("http://growattreader:5000/update_aggregated_data")
        if response.status_code == 200:
            cleaner.log_it("BKW-agg", "Success")
            cleaner.sync_BKW_data_with_drive("BKW-agg")

        else:
            print(f"Failed to read data, status code: {response.status_code}")
            cleaner.log_it("BKW-agg", "Failure")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily", "Exception", Exception=e)


schedule.every(2).minutes.do(read_the_BKW_daily)
schedule.every(2).minutes.do(read_the_BKW_aggregated)
schedule.every(1).hours.do(cleaner.sync_log_data_with_drive)


cleaner.log_it("Pulse", "Initiate")
while True:
    schedule.run_pending()
