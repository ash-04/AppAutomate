import time
from appium.webdriver.common.touch_action import TouchAction


exception_string = "There is a error of"


def is_tap(driver, x, y):
    # create object for Action class
    user_action = TouchAction(driver)
    time.sleep(2)

    try:
        user_action.tap(x=x, y=y).perform()

    except Exception as e:
        print(exception_string, str(e))
        print('element not present')
        return False
    return True


def is_swipe(driver, x, y, w, z):
    # create object for Action class
    user_action = TouchAction(driver)
    time.sleep(2)

    try:
        user_action.press(x=x, y=y).move_to(x=w, y=z).release().perform()

    except Exception as e:
        print(exception_string, str(e))
        print('element not present')
        return False
    return True

