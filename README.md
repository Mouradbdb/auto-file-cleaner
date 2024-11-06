# Auto Delete Old Files

This project is a Python-based solution that automatically deletes files older than 24 hours from a specified folder. It is designed to help manage files like screenshots, which should be cleaned up regularly without manual intervention.

## Features:
- Monitors a designated folder for files older than 24 hours.
- Automatically deletes files that exceed the 24-hour age limit.
- Runs continuously in the background using Python.
- Can be set up to run as a background process using Task Scheduler.
## Requirements:
- Python 3.x installed on your system.
- The script uses built-in Python libraries: `os`, `time`.

## How to Use:
1. **Download or Clone the Repository:**
   Download the repository or clone it to your local machine.

2. **Set the Folder Path:**
   Update the `folder_path` variable in the Python script to point to the folder where your files (e.g., screenshots) are stored.

3. **Run the Python Script:**
   Simply run the `delete_old_files.py` script using Python:
   ```bash
   python delete_old_files.py
   ```
 4. **Set Up for Continuous Background Execution Using Task Scheduler:**
   To ensure that the script runs continuously in the background, even after a system reboot or login, you can set it up to run automatically using Windows Task Scheduler.

   ### Steps to Set Up Task Scheduler:
   
   1. **Create a Batch File to Run the Python Script:**
      - Open Notepad and paste the following code:
      ```batch
      @echo off
      pythonw C:\path\to\your\script\delete_old_files.py
      ```
      - Replace `C:\path\to\your\script\delete_old_files.py` with the actual path to your Python script.
      - Save this file as `run_script.bat`.
   
   2. **Open Task Scheduler:**
      - Type "Task Scheduler" in the Start Menu search bar and open it.
   
   3. **Create a New Task:**
      - In Task Scheduler, click on **Create Basic Task** from the right-hand panel.
      - Give the task a name, such as "Delete Old Files", and click **Next**.
   
   4. **Set Trigger to Run the Script at Logon:**
      - Select **When I log on** as the trigger and click **Next**.
      - This ensures that the script will run every time you log into your computer.
   
   5. **Choose Action to Start the Program:**
      - Select **Start a Program** as the action and click **Next**.
      - Browse to select the `run_script.bat` file you created earlier.
   
   6. **Finish the Task Setup:**
      - Click **Finish** to save the task. The script will now be set to run automatically whenever you log into your computer.

   7. **Configure the Task to Run Continuously:**
      - In Task Scheduler, locate your task (e.g., "Delete Old Files") in the **Task Scheduler Library**.
      - Right-click on the task and select **Properties**.
      - In the **General** tab, check the box **Run with highest privileges** to ensure the task has the necessary permissions.
      - In the **Triggers** tab, click **Edit** and adjust the settings to **Repeat task every** 1 minute for **Indefinitely**. This ensures the task runs continuously in the background and performs the file check at the specified interval.

   The task is now set up to run in the background, ensuring that the script will continue to check the folder and delete old files as needed.
