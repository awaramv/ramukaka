import schedule
import time
import requests
import file_manager


def read_the_BKW_daily():
    try:
        response = requests.get("http://growattreader:5000/update_daily_data")
        if response.status_code == 200:
            file_manager.log_it("BKW-daily", "Success")
            file_manager.sync_BKW_data_with_drive("BKW-daily")

        else:
            file_manager.log_it("BKW-daily", "Failure")
    except requests.exceptions.RequestException as e:
        file_manager.log_it("BKW-daily", "Exception", Exception=e)


def read_the_BKW_aggregated():
    try:
        response = requests.get("http://growattreader:5000/update_aggregated_data")
        if response.status_code == 200:
            file_manager.log_it("BKW-agg", "Success")
            file_manager.sync_BKW_data_with_drive("BKW-agg")

        else:
            print(f"Failed to read data, status code: {response.status_code}")
            file_manager.log_it("BKW-agg", "Failure")
    except requests.exceptions.RequestException as e:
        file_manager.log_it("BKW-daily", "Exception", Exception=e)


schedule.every(2).minutes.do(read_the_BKW_daily)
schedule.every(2).minutes.do(read_the_BKW_aggregated)
schedule.every(1).hours.do(file_manager.sync_log_data_with_drive)

while True:
    file_manager.log_it("Pulse", "Success")
    schedule.run_pending()
    time.sleep(300)
