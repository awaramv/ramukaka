import shutil
from datetime import datetime
import os
from zoneinfo import ZoneInfo


LOG_FILE = "./logs/scheduler.txt"
BKA_DAILY_FILE = "./logs/daily_detailed_power_output.csv"
BKA_AGG_FILE = "./logs/aggregated_power_output.csv"
DESTINATION = "/home/awara/mnt/GoogleDrive/PiDumps"
# DESTINATION = "../mnt/GoogleDrive/PiDumps"


def sync_BKW_data_with_drive(mode):
    if mode == "BKW-daily":
        src_file = BKA_DAILY_FILE
        try:
            os.makedirs(DESTINATION, exist_ok=True)
            shutil.copy2(src_file,
                        os.path.join(DESTINATION,
                        os.path.basename(src_file)))
            log_it("DriveSync-BKW-daily", "Success")
        except Exception as e:
            log_it("DriveSync-BKW-daily", "Exception", Exception=e)

    if mode == "BKW-agg":
        src_file = BKA_AGG_FILE
        try:
            shutil.copy2(src_file,
                        os.path.join(DESTINATION,
                        os.path.basename(src_file)))
            log_it("DriveSync-BKW-agg",  "Success")
        except Exception as e:
            log_it("DriveSync-BKW-agg", "Exception", Exception=e)


def log_it(mode, outcome, Exception=None):
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    if mode == "Pulse":
        if outcome == "Initiate":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Scheduler Initiated\n")
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Scheduler checked for the Jobs\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Scheduler failed to check for Jobs\n")

    elif mode == "BKW-agg":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Data read from BKW Aggregated\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Failed to read Data read from BKW Aggregated\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Exception occurred for BKA Aggregated: {Exception}\n")

    elif mode == "BKW-daily":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Data read from BKW daily\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Failed to read Data read from BKW Daily\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Exception occurred for BKW Daily: {Exception}\n")

    elif mode == "DriveSync-BKW-daily":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : BKW Daily Data file synced successfully\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Failed to sync BKW Daily data file\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Exception occurred for BKA Daily Drive sync: {Exception}\n")

    elif mode == "DriveSync-BKW-agg":
        if outcome == "Success":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : BKW Aggregated File synced successfully\n")
        elif outcome == "Failure":
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Failed to sync BKW aggregated file\n")
        elif Exception is not None:
            with open(LOG_FILE, "a+") as f:
                f.write(f"{now} : Exception occurred for BKW Aggregated Drive sync : {Exception}\n")


def sync_log_data_with_drive():
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    src_file = "/home/awara/dockersinit/logs/scheduler.txt"

    try:
        shutil.copy2(src_file,
                    os.path.join(DESTINATION,
                    os.path.basename(src_file)))
        print(f"Log file synced successfully at {now}")
        log_it("DriveSync", "Success")
    except Exception as e:
        print(f"An error occurred while syncing files: {e} at {now}")
        log_it("DriveSync", "Failure")
