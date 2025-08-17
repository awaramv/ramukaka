import shutil


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
