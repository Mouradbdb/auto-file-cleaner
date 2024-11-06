import os
import time
import sys

# Set the folder where you want to store the files to be deleted!
folder_path = r'C:\Temp_Files'

lock_file = 'script.lock'

# Check if the lock file exists, which means the script is already running
if os.path.exists(lock_file):
    print("Another instance of the script is already running.")
    sys.exit()
    
# Create the lock file to indicate that the script is running
with open(lock_file, 'w') as f:
    f.write('')

# Set the time limit (24 hours in seconds)
time_limit = 24 * 60 * 60  # 24 hours in seconds you can changethe time (in seconds)

def delete_old_files():
    current_time = time.time()
    
    # Loop through all the files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a folder) and check the last modified time
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            
            # If the file is older than 24 hours, delete it
            if file_age > time_limit:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# Run the script continuously
try:
    while True:
        delete_old_files()
        # Sleep for 1 minute before checking again
        time.sleep(60)

finally:
    # Remove the lock file when the script finishes
    os.remove(lock_file)