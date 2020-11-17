# **Magister API**
## **Summary:**
This is a implementation for the Magister private API. You can(for now) use it to fetch a school roster and apitoken. This is done by using a headless selenium instance. 


- [**Magister API**](#magister-api)
  - [**Summary:**](#summary)
  - [**Setup:**](#setup)
  - [**Usage:**](#usage)
    - [**Authentication:**](#authentication)
    - [**Rooster:**](#rooster)
  - [**TODO:**](#todo)

---
## **Setup:**
You need to host this api on your own webserver, or you can run it on your own machine. It is not intended for heavy use, and it's not effective at all. The fetching takes around 30 second for the api key. You can use this key for a few hours.  

**Step 1: Clone the repository:**  

    git clone https://github.com/maantjemol/magister-api-python
    cd magister-api-python

**Step 2: Create an environment and install requirements:**

    python3 -m venv venv
    pip3 install -r requirements.txt

**Step 3: Start `server.py`**

    python3 server.py
---
## **Usage:**
You can make requests to **`http://localhost:5000`**. The currently implemented request are:

### **Authentication:**  
Base url:
**`/api/auth`**  
| Parameter:  | Example: |
| :---        |    :----:   |
| username | 234543 |
| password | weakPassword123 |
| school | ErasmusCollege |

Example url: `/api/auth?username=234543&password=weakPassword&school=ErasmusCollege`  
Response:

    {
        "accessToken": "token"
    }

***NOTE:**
This request will take about 30 seconds*

### **Rooster:**  
Base url:
**`/api/rooster`**  
| Parameter:  | Example: |
| :---        |    :----:   |
| dateFrom | 2020-09-25|
| dateTill | 2020-10-02 |
| school | ErasmusCollege |
| apitoken | API token you received in previous request |

Example url: `/api/rooster?dateFrom=2020-09-25&dateTill=2020-10-02&school=ErasmusCollege&apitoken=<token you received>`  
Response:  

    {
    "Items": [
    ...

---
## **TODO:**
- [x] Add auth page
- [x] Split roster and authentication
- [x] Add grades
- [x] Deploy it to a docker container
- [ ] Add grades instructions
- [ ] Add docker instructions
- [ ] Add security
- [ ] Make it cross platform