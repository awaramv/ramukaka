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
            cleaner.log_it("BKW-daily", "Failure")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily", "Exception", Exception=e)


def read_the_BKW_aggregated():
    try:
        response = requests.get("http://growattreader:5000/update_aggregated_data")
        if response.status_code == 200:
            cleaner.log_it("BKW-agg", "Success")
        else:
            print(f"Failed to read data, status code: {response.status_code}")
            cleaner.log_it("BKW-agg", "Failure")
    except requests.exceptions.RequestException as e:
        cleaner.log_it("BKW-daily", "Exception", Exception=e)


schedule.every().day.at("23:00").do(read_the_BKW_daily)
schedule.every().day.at("23:15").do(read_the_BKW_aggregated)
schedule.every().day.at("23:30").do(cleaner.sync_log_data_with_drive)

cleaner.log_it("Pulse", "Initiate")
while True:
    schedule.run_pending()
