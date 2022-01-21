from selenium import webdriver
import time
import Locators
import SiteURL


def novimim(lmail, sifra):
    driver = webdriver.Chrome()
    driver.get(SiteURL.HOME_URL)
    prijaviSe = driver.find_element_by_css_selector(Locators.Prijavi_Se)
    prijaviSe.click()

    poljeLmail = driver.find_element_by_css_selector(
        Locators.Polje_Login_lemail)
    poljeSifra = driver.find_element_by_css_selector(
        Locators.Polje_Login_sifra)

    dugmeUlogujSe = driver.find_element_by_css_selector(Locators.Uloguj_Se)

    poljeLmail.send_keys(lmail)
    poljeSifra.send_keys(sifra)
    dugmeUlogujSe.click()

    time.sleep(3)

    slikaMima = driver.find_element_by_xpath(Locators.slika_Mima)
    slika1 = slikaMima.get_attribute("src")
    print("------", slika1)

    dugmeNoviMim = driver.find_element_by_xpath(Locators.Novi_Mim)
    dugmeNoviMim.click()

    time.sleep(4)
    slikaMima = driver.find_element_by_xpath(Locators.slika_Mima)
    slika2 = slikaMima.get_attribute("src")
    print("------", slika2)

    if slika1 != slika2:
        print("To bracala")
    else:
        print("Slike su iste ")


novimim("cmcnally0@usa.gov", "sKwkqGD4RwN")
