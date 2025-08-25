import shutil
import datetime

LOG_FILE = "./logs/scheduler.txt"
BKA_DAILY_FILE = "./logs/daily_detailed_power_output.csv"
BKA_AGG_FILE = "./logs/aggregated_power_output.csv"
DESTINATION = "/home/awara/mnt/GoogleDrive/PiDumps"


def sync_BKW_data_with_drive(mode):
    if mode == "BKW-daily":
        src_file = BKA_DAILY_FILE
        dest = DESTINATION
        try:
            shutil.copy(src_file, dest)
            log_it("DriveSync-BKW-daily", "Success")
        except Exception as e:
            log_it("DriveSync-BKW-daily", "Exception", Exception=e)

    if mode == "BKW-agg":
        src_file = BKA_AGG_FILE
        dest = DESTINATION
        try:
            shutil.copy(src_file, dest)
            log_it("DriveSync-BKW-agg",  "Success")
        except Exception as e:
            log_it("DriveSync-BKW-agg", "Exception", Exception=e)


def log_it(mode, outcome, Exception=None):
    now = datetime.datetime.now()
    if mode == "Pulse":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Scheduler checked for the Jobs last at {now} \n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Scheduler failed to check for the Jobs last at {now}\n")

    elif mode == "BKW-agg":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Data read from BKW at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to read Data read from BKW at {now}\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"Exception occurred: {Exception} at {now}\n")

    elif mode == "BKW-daily":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Data read from BKW at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to read Data read from BKW at {now}\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"Exception occurred: {Exception} at {now}\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"Exception occurred: {Exception} at {now}\n")

    elif mode == "DriveSync-BKW-daily":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"BKW Daily Data file synced successfully at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to sync BKW Daily data file at {now}\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"Exception occurred: {Exception} at {now}\n")

    elif mode == "DriveSync-BKW-agg":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"File synced successfully at {now}\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"Failed to sync files at {now}\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"Exception occurred: {Exception} at {now}\n")


def sync_log_data_with_drive():
    now = datetime.datetime.now()
    src_file = "/home/awara/dockersinit/logs/scheduler.txt"
    dest = "/home/awara/mnt/GoogleDrive/PiDumps"

    try:
        shutil.copy(src_file, dest)
        print(f"Log file synced successfully at {now}")
        log_it("DriveSync", "Success")
    except Exception as e:
        print(f"An error occurred while syncing files: {e} at {now}")
        log_it("DriveSync", "Failure")
