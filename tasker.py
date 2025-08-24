import schedule
import time
import datetime
import requests
import file_manager

LOG_FILE = "./logs/scheduler.txt"


def read_the_BKW():
    now = datetime.datetime.now()
    try:
        response = requests.get("http://growattreader:5000/update_data")
        if response.status_code == 200:
            data = response.json()
            print(f"Data read successfully: {data}")
            file_manager.sync_BKW_data_with_drive()
            print(f"Data synced with Google Drive at {datetime.datetime.now()}")
            with open(LOG_FILE, "a+") as f:
                f.write(f"Data read from BKW and Saved to Google Drive at : {now}\n")
        else:
            print(f"Failed to read data, status code: {response.status_code}")
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to read Data read from BKW  : {now}\n")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while reading data: {e}")


schedule.every().day.at("00:00").do(read_the_BKW)


def write_current_datetime_to_file():
    now = datetime.datetime.now()
    with open(LOG_FILE, "a+") as f:
        f.write(f"Scheduler checked for the Jobs last at : {now}\n")
    print(f"Date and time written at {now} to {LOG_FILE}")


while True:
    write_current_datetime_to_file()
    schedule.run_pending()
    time.sleep(60)
