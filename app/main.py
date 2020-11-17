import requests
from apitoken import getApiToken


def accesstoken(username, password, school):
    # Starting session
    # Getting API-token from apitoken.py
    accessToken = getApiToken(username, password, school)
    return {"accessToken": accessToken}


def rooster(school, dateFrom, dateTill, apitoken):
    session = requests.session()
    burp0_url = "https://" + school + \
        ".magister.net:443/api/personen/9522/afspraken?status=1&tot="+dateTill+"&van="+dateFrom
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5",
                     "Accept-Encoding": "gzip, deflate", "Authorization": "Bearer " + apitoken, "Connection": "close", "Referer": "https://zandvliet.magister.net/magister/"}
    r = session.get(burp0_url, headers=burp0_headers)
    return r.json()


def grades(school, apitoken, dateFrom=None, dateTill=None):
    if dateFrom == None or dateTill == None:
        url = "https://"+school + \
            ".magister.net:443/api/personen/9520/cijfers/laatste?top=50&skip=0"
    else:
        url = "https://"+school+".magister.net:443/api/leerlingen/9520/aanmeldingen?begin=" + \
            dateFrom+"&einde="+dateTill
    headers = {"Connection": "close", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer " + apitoken,
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://"+school+".magister.net/magister/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == '__main__':
    print("executing main")
    print(grades("zandvliet", "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFDNTUyQ0VFMTNEQzc1MjkwOUU4QjhBQjU3MjA3MUQzODk2Mzg1NTNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkhGVXM3aFBjZFNrSjZMaXJWeUJ4MDRsamhWTSJ9.eyJuYmYiOjE2MDU1NDk1NjQsImV4cCI6MTYwNTU1MzE2NCwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5tYWdpc3Rlci5uZXQiLCJhdWQiOiJodHRwczovL2FjY291bnRzLm1hZ2lzdGVyLm5ldC9yZXNvdXJjZXMiLCJjbGllbnRfaWQiOiJNNi16YW5kdmxpZXQubWFnaXN0ZXIubmV0Iiwic3ViIjoiYWZkZjA0YTU0NWM4NDY1NzgxNzEwODFjMmNkODIwNDMiLCJhdXRoX3RpbWUiOjE2MDU1NDk1NjQsImlkcCI6ImxvY2FsIiwidGlkIjoiMjU2M2Y5YzYzN2RhNDJlYjkwNzczNmE0MTRlMTdkZTciLCJ1cm46bWFnaXN0ZXI6Y2xhaW1zOmlhbTp0ZW5hbnRJZCI6IjI1NjNmOWM2MzdkYTQyZWI5MDc3MzZhNDE0ZTE3ZGU3IiwidXJuOm1hZ2lzdGVyOnRpZCI6IjI1NjNmOWM2MzdkYTQyZWI5MDc3MzZhNDE0ZTE3ZGU3IiwidXJuOm1hZ2lzdGVyOmNsYWltczppYW06dGVuYW50IjoiemFuZHZsaWV0Lm1hZ2lzdGVyLm5ldCIsInVybjptYWdpc3RlcjpjbGFpbXM6aWFtOnVzZXJuYW1lIjoiMjA1MTY0IiwianRpIjoiNTNFRUZENTlEN0Y3NEQ2NkJCQ0UyMjlERjQ5MzQ3MTAiLCJzaWQiOiJBNjc0RjUwNEYwMzdDMUFGRThCMTg1NENCRDAxNTk3NiIsImlhdCI6MTYwNTU0OTU2NCwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSJdLCJhbXIiOlsicHdkIl19.gfKm48tUgsW6MiiOPyWbUPi1Dk2x0jN6Bo4__WxDGsLvRF2cxX1pSG3eCHWfVlNxS89yybEEIfLPrPQf1PUm3lJ4-yGrgLNJPf5WNQhDoG2baM1nIv6LxhEyz5Ri7BQKxH0falKx5vkQW4YTFMfCEoN_glAx21BIRSpPakhCQvYH-awmYG1BgBLs3EaJEkCpng8B72Igl_TF4bDWFoXMtVk_7OyLS5X7XkNxrGPBxaV6n9HiQOe_dNUo1ZzwMc_jBkIpLrlUGCftWNAMVn6nk6xXw4xY_24JOU5-1dkrnnyZqskivrV9RpyIt_4PZtObZU7JL4qSsm16qOle95hKnw"))
