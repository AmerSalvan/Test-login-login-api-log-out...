from selenium import webdriver
import time
import Locators
import SiteURL


def loginTest(lmail, sifra):
    driver = webdriver.Chrome()
    driver.get(SiteURL.HOME_URL)
    prijaviSe = driver.find_element_by_css_selector(Locators.Prijavi_Se)
    prijaviSe.click()

    poljeLmail = driver.find_element_by_css_selector(Locators.Polje_Login_lemail)
    poljeSifra = driver.find_element_by_css_selector(Locators.Polje_Login_sifra)

    dugmeUlogujSe = driver.find_element_by_css_selector(Locators.Uloguj_Se)

    poljeLmail.send_keys(lmail)
    poljeSifra.send_keys(sifra)
    dugmeUlogujSe.click()

    time.sleep(3)

    dugmeOdjaviSe = driver.find_element_by_css_selector(Locators.Odjavi_Se)
    dugmeOdjaviSe.click()

    time.sleep(3)
    
    prijaviSe = driver.find_element_by_css_selector(Locators.Prijavi_Se)
    print(prijaviSe.text)

    if prijaviSe.text == "Prijavi se":
        print("Uspesan logout")
    else:
        print("Neuspesan logout")

loginTest("cmcnally0@usa.gov", "sKwkqGD4RwN")