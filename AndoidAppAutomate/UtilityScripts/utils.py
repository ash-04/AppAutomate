import time

from appium import webdriver
from Locators.login import *
from Locators.select_group import *
from Locators.create_group import *
from UtilityScripts.helper import is_tap, is_swipe
from resources.constants import *


def get_driver():
    # Define the capabilities for Android app automation
    desired_caps = {
        "platformName": PLATFORM,
        "appium:deviceName": DEVICE_NAME,
        "appium:appPackage": APP_PACKAGE,
        "appium:appActivity": APP_ACTIVITY,
        "noReset": NO_RESET
    }

    # Initialize the WebDriver with BrowserStack's remote URL
    driver = webdriver.Remote(
        "http://localhost:4723/wd/hub", desired_caps)

    return driver


def launch_app(driver):
    """
        Function to launch the android app
        :return:
    """

    try:
        is_tap(driver, login_click[0], login_click[1])
        is_tap(driver, login_first_number[0], login_first_number[1])
        is_tap(driver, login_second_number[0], login_second_number[1])
        is_tap(driver, login_third_number[0], login_third_number[1])
        is_tap(driver, login_fouth_number[0], login_fouth_number[1])
        is_tap(driver, login_fifth_number[0], login_fifth_number[1])
        is_tap(driver, login_submit_button[0], login_submit_button[1])

    except Exception as e:
        print(e)


def select_group(driver):
    """
        Function to launch the android app
        :return:
    """

    try:
        is_tap(driver, groups_icon[0], groups_icon[1])
        is_tap(driver, add_icon[0], add_icon[1])
        is_tap(driver, first_mem[0], first_mem[1])
        is_tap(driver, second_mem[0], second_mem[1])
        is_tap(driver, next_button[0], next_button[1])

    except Exception as e:
        print(e)


def create_group(driver):
    """
        Function to launch the android app
        :return:
    """

    try:
        time.sleep(3)
        is_tap(driver, grp_name[0], grp_name[1])
        is_tap(driver, char_1[0], char_1[1])
        is_tap(driver, char_2[0], char_2[1])
        is_tap(driver, char_3[0], char_3[1])
        is_tap(driver, char_4[0], char_4[1])
        is_tap(driver, rec_check[0], rec_check[1])
        is_tap(driver, rec_days[0], rec_days[1])
        is_swipe(driver, swipe_press[0], swipe_press[1], swipe_move[0], swipe_move[1])
        is_tap(driver, confirm_button[0], confirm_button[1])
        is_tap(driver, submit[0], submit[1])

    except Exception as e:
        print(e)


def close_server(driver):
    time.sleep(5)
    driver.quit()
