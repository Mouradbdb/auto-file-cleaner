import os
import time

# Set the folder where you want to store the files to be deleted!
folder_path = r'C:\Temp_Files'

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
while True:
    delete_old_files()
    # Sleep for 1 minute before checking again
    time.sleep(60)
