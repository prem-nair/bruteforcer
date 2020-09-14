import requests

from bruty import BruteManager

brute = BruteManager()
brute.start()

def check():
    session = requests.Session()
    session.get("https://www.google.com")
    