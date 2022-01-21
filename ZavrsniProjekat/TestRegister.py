from selenium import webdriver
import time
import SiteURL
import Locators
import MockData


def registerOnaWebsite(ime, mail, sifra):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(SiteURL.HOME_URL)
    time.sleep(2)
    prijaviSeDugme = driver.find_element_by_css_selector(Locators.Prijavi_Se)
    prijaviSeDugme.click()

    registrujteSe = driver.find_element_by_css_selector(Locators.Registruj_Se)
    registrujteSe.click()

    poljeIme = driver.find_element_by_xpath(Locators.Polje_IME)
    poljeEmail = driver.find_element_by_xpath(Locators.Polje_Email)
    poljeSifra = driver.find_element_by_css_selector(Locators.Polje_Sifra)
    poljePotvrdaSifre = driver.find_element_by_css_selector(Locators.Polje_Ponovi_Sifru)

    dugmeRegistrujSe = driver.find_element_by_class_name(Locators.Registruj_Se_Ovde)
    
    poljeIme.send_keys(ime)
    poljeEmail.send_keys(mail)
    poljeSifra.send_keys(sifra)
    poljePotvrdaSifre.send_keys(sifra)
    
    time.sleep(2)

    dugmeRegistrujSe.click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    
    ok = driver.find_element_by_xpath(Locators.OK)
    print(ok.text)

    if ok.text == "OK":
        print(f"Uspesno si se registrovo sa {ime} i {mail}")
    else:
        print("Ne uspesan login")

    
registerOnaWebsite("askrfgw0aw3s3qs99swi","agfd99gw33as0dse@sforad.rs","Amer1234")

#for data in MockData.Test_Data:
    #registerOnaWebsite(data["ime"],data["mail"],data["sifra"])
    

