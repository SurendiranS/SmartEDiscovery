# SmartEDiscovery

## Description

This a demostration of the use of LLM's for the purpose of E-discovery in Cyber-forensic.  This Project uses the Reverse engineered Google BARD API  by https://github.com/acheong08/Bard.

## Authentication
> **Warning** Do not expose the `__Secure-1PSID` 
1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API key for convenience, it is not an officially provided API key. 
Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.
<br>

## Dependencies
* python-docx
* httpx

## Running the Code
To install the requirements for this project, run the following command:
```bash
$ pip install -r requirements.txt
```
To use this project, run the [discover.py](https://github.com/SurendiranS/SmartEDiscovery/blob/main/src/discover.py) script 
```bash
$ python3 /src/discover.py
```

![Screenshot 2023-06-06 121538](https://github.com/SurendiranS/SmartEDiscovery/assets/43315429/0eaf8ae1-a57f-481f-856b-aa1118b6893b)
