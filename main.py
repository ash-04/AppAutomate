import time

from UtilityScripts.utils import get_driver, launch_app, select_group, create_group, close_server


if __name__ == "__main__":
    try:
        driver = get_driver()
        time.sleep(10)
        launch_app(driver)
        select_group(driver)
        create_group(driver)
        close_server(driver)

    except Exception as e:
        print(f"Exception occured due to {e}")



