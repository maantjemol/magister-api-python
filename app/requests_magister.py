from os import name
import requests
from apitoken import getApiToken


def accesstoken(username, password, school):
    # Starting session
    # Getting API-token from apitoken.py
    accessToken = getApiToken(username, password, school)
    return accessToken


def rooster(school, dateFrom, dateTill, apitoken, personId):
    session = requests.session()
    burp0_url = "https://" + school + \
        ".magister.net:443/api/personen/"+personId + \
        "/afspraken?status=1&tot="+dateTill+"&van="+dateFrom
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5",
                     "Accept-Encoding": "gzip, deflate", "Authorization": "Bearer " + apitoken, "Connection": "close", "Referer": "https://"+school+".magister.net/magister/"}
    r = session.get(burp0_url, headers=burp0_headers)
    return r.json()


def grades(school, apitoken, personId, dateFrom=None, dateTill=None):
    if dateFrom == None or dateTill == None:
        url = "https://"+school+".magister.net:443/api/personen/" + \
            personId + "/cijfers/laatste?top=25&skip=0"
    else:
        url = "https://"+school+".magister.net:443/api/leerlingen/"+personId+"/aanmeldingen?begin=" + \
            dateFrom+"&einde="+dateTill
    header = {"Connection": "close", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer " + apitoken,
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://"+school+".magister.net/magister/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    r = requests.get(url, headers=header)
    # print(r.text)
    return r.json()