import requests
import SiteURL
import MockData


def login_API(mali, sifra):
    requsetData = {
        "email":mali,
        "password":sifra
    }
    response = requests.post(SiteURL.LOGIN_URL_API,requsetData)
    print(response.status_code)
    if response.status_code == 200:
        print("Uspesan login")
        responseData = response.json()
        print(responseData)
        print("JWT je ---", responseData["token"])
    else:
        print("Los email ili sifra")

#login_API("edes@code.rs","Amers1234")

for element in MockData.TEST_DATA2:
    login_API(element["email"],element["sifra"])
