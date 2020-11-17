from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from seleniumwire import webdriver
import os
import platform
# Importing libraries


def getApiToken(user, passwd, school):
    # Adding chrome driver, and launching it in headless mode:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    if platform.system() == "Windows":
        chrome_driver = os.getcwd() + "\\app\\chromedriver.exe"
    if platform.system() == "Linux":
        chrome_driver = os.getcwd() + "/chromedriver"
        # chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

    # Uncomment for Firefox GUI webdriver:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome(
        chrome_options=chrome_options, executable_path=chrome_driver)
    # Navigating to Magister and loging in,
    # Grabbing the accestoken for the private API:
    driver.get("https://" + school + ".magister.net")
    driver.implicitly_wait(3)
    elem = driver.find_element_by_id("username")
    elem.clear()
    elem.send_keys(user)
    elem.send_keys(Keys.RETURN)
    sleep(0.5)
    elem = driver.find_element_by_id("password")
    elem.clear()
    elem.send_keys(passwd)
    elem.send_keys(Keys.RETURN)
    sleep(2)
    # Filtering out the request with the API token, and parsing the request:
    hiturl = "https://accounts.magister.net/connect/authorize/callback?client_id=M6-zandvliet.magister.net"
    for request in driver.requests:
        if request.response:
            if hiturl in request.url:
                driver.quit()
                return request.response.headers["location"].split("access_token=", 1)[1].split("&")[0]

