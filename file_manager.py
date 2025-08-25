import shutil
import datetime

LOG_FILE = "./logs/scheduler.txt"

def sync_BKW_data_with_drive():
    src_file = "/home/awara/dockersinit/logs/daily_detailed_power_output.csv"
    dest_file = "/home/awara/mnt/GoogleDrive/PiDumps/daily_detailed_power_output.csv"
    try:
        shutil.copy(src_file, dest_file)
        print(f"File synced successfully from {src_file} to {dest_file}")
        log_it("BKW", "Success")
    except Exception as e:
        print(f"An error occurred while syncing files: {e}")
        log_it("DriveSync", "Failure")

    src_file = "/home/awara/dockersinit/logs/aggregated_power_output.csv"
    dest_file = "/home/awara/mnt/GoogleDrive/PiDumps/aggregated_power_output.csv"

    try:
        shutil.copy(src_file, dest_file)
        print(f"File synced successfully from {src_file} to {dest_file}")
        log_it("BKW", "Success")
    except Exception as e:
        print(f"An error occurred while syncing files: {e}")
        log_it("DriveSync", "Failure")


def log_it(mode, outcome):
    now = datetime.datetime.now()
    if mode == "Pulse":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write("Scheduler checked for the Jobs last at : {now} \n")
    elif mode == "BKW":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Data read from BKW at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to read Data read from BKW at {now}\n")
    elif mode == "DriveSync":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"File synced successfully at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to sync files at {now}\n")


def sync_log_data_with_drive():
    now = datetime.datetime.now()
    src_file = "/home/awara/dockersinit/logs/scheduler.txt"
    dest_file = "/home/awara/mnt/GoogleDrive/PiDumps/scheduler.txt"

    try:
        shutil.copy(src_file, dest_file)
        print(f"Log file synced successfully at {now}")
        log_it("DriveSync", "Success")
    except Exception as e:
        print(f"An error occurred while syncing files: {e} at {now}")
        log_it("DriveSync", "Failure")
