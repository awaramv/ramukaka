import schedule
import time
import datetime
import requests
import shutil

def read_the_BKW():
    try:
        response = requests.get("https://growattreader:80/update_data")
        if response.status_code == 200:
            data = response.json()
            print(f"Data read successfully: {data}")
        else:
            print(f"Failed to read data, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while reading data: {e}")
        sync_BKW_data_with_drive()


schedule.every().day.at("23:00").do(read_the_BKW)


def sync_BKW_data_with_drive():
    dest_file = "/home/awara/mnt/GoogleDrive/PiDumps"

    src_file = "/home/awara/dockersinit/logs/daily_detailed_power_output.csv"
    try:
        shutil.copy(src_file, dest_file)
        print(f"File synced successfully from {src_file} to {dest_file}")
    except Exception as e:
        print(f"An error occurred while syncing files: {e}")

    src_file = "/home/awara/dockersinit/logs/aggregated_power_output.csv"
    try:
        shutil.copy(src_file, dest_file)
        print(f"File synced successfully from {src_file} to {dest_file}")
    except Exception as e:
        print(f"An error occurred while syncing files: {e}")


while True:
    schedule.run_pending()
    time.sleep(60)
    # Sleep for 60 seconds before checking again
