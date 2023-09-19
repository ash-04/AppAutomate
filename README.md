# Purpose

 To validate one user journey with the following steps

- launch a preinstalled app
- Enter pin for login 
- Click on Groups icon
- Select new group icon
- Add memebers of the group from the existing friend list
- Click on the proceed button
- Enter group name
- Select recurring settlement button
- Add a date for settlement
- Click on submit button to create the group


# How to run script locally

1. Create a venv environment
    - Reference: https://docs.python.org/3/library/venv.html)

2. Install packages in the `requirements.txt` through pip 
    - Run Command: `pip install -r requirements.txt` 

3. Run script

   - python main.py


# Prerequisite

- Install Appium server and required steps mentioned here :
  https://appiumpro.com/editions/91-getting-started-with-appium-for-android-on-windows

- Launch appium server during the execution to capture logs


# Limitations

- Currently the implementation of the code is compatible with Pixel 7 only, so create a VDM as Pixel 7
- When the device is created and launched, open cmd and run adb.devices to check the device name 
- Replace the device name in 'DEVICE_NAME' in resources/constants.py

