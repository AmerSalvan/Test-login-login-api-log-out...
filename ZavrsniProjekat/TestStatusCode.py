import requests
import SiteURL


def isOnlin(site):
    website = requests.get(site, timeout=10)
    print()
    if website.status_code == 200:
        print(website)
        return True
    else:
        False
     

if isOnlin(SiteURL.HOME_URL) == True:
    print("Sajt je onlin")
else:
    print("nije online")
    
