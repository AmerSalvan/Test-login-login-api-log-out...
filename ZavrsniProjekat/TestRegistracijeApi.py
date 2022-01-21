import requests
import SiteURL
import MockData

def registracijaAPI(ime, mail, sifra):
    requestsData = {
        "username":ime,
        "email":mail,
        "password":sifra
    }
    response = requests.post(SiteURL.Registracija_URL_API, requestsData)
    print(response.status_code)
    if response.status_code == 201:
        print("Uspesna registracija")
    else:
        print("no")


registracijaAPI("amessrsssa","edses@caosde.rs","Amers1234")

