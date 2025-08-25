import schedule
import time
import datetime
import requests
import file_manager

def read_the_BKW():
    now = datetime.datetime.now()
    try:
        response = requests.get("http://growattreader:5000/update_data")
        if response.status_code == 200:
            file_manager.log_it("BKW", "Success")
            file_manager.sync_BKW_data_with_drive()

        else:
            print(f"Failed to read data, status code: {response.status_code}")
            file_manager.log_it("BKW", "Failure")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while reading data: {e}")


schedule.every(10).minutes.do(read_the_BKW)

schedule.every(1).hours.do(file_manager.sync_log_data_with_drive)

while True:
    file_manager.log_it("Pulse", "Success")
    schedule.run_pending()
    time.sleep(300)
