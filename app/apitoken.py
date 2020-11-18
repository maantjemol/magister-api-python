from os import name
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from seleniumwire import webdriver
import os
import platform
import requests
# Importing libraries


def personId(school, apitoken):
    url = "https://"+school+".magister.net:443/api/toestemmingen"
    header = {"Connection": "close", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer " + apitoken,
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://"+school+".magister.net/magister/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    r = requests.get(url, headers=header)
    return r.json()["items"][0]["persoonId"]


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
    hiturl = "https://accounts.magister.net/connect/authorize/callback?client_id=M6-" + \
        school+".magister.net"
    for request in driver.requests:
        if request.response:
            if hiturl in request.url:
                driver.quit()
                accestoken = request.response.headers["location"].split("access_token=", 1)[
                    1].split("&")[0]
                id = personId(school, accestoken)
                return {"apitoken": accestoken, "personID": id}
