import schedule
import time
import datetime
import requests
import file_manager


def read_the_BKW():
    try:
        response = requests.get("http://growattreader:5000/update_data")
        if response.status_code == 200:
            data = response.json()
            print(f"Data read successfully: {data}")
            file_manager.sync_BKW_data_with_drive()
            print(f"Data synced with Google Drive at {datetime.datetime.now()}")
        else:
            print(f"Failed to read data, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while reading data: {e}")


schedule.every().day.at("23:30").do(read_the_BKW)


while True:
    schedule.run_pending()
    time.sleep(60)
    # Sleep for 60 seconds before checking again
