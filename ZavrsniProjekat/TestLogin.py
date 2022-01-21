from selenium import webdriver
import time
import Locators
import SiteURL
import MockData


def loginTest(mail, sifra):
    driver = webdriver.Chrome()
    driver.get(SiteURL.HOME_URL)
    prijaviSe = driver.find_element_by_css_selector(Locators.Prijavi_Se)
    prijaviSe.click()

    poljeLmail = driver.find_element_by_css_selector(
        Locators.Polje_Login_lemail)
    poljeSifra = driver.find_element_by_css_selector(
        Locators.Polje_Login_sifra)

    dugmeUlogujSe = driver.find_element_by_css_selector(Locators.Uloguj_Se)

    poljeLmail.send_keys(mail)
    poljeSifra.send_keys(sifra)
    dugmeUlogujSe.click()

    time.sleep(3)

    #naslov = driver.find_element_by_xpath(Locators.naslov)

    #dugmeNoviMim = driver.find_element_by_class_name(Locators.Novi_Mim)
    #dugmeNoviMim.click()

    time.sleep(3)
    

    if driver.current_url == SiteURL.HEJ_URL:
        print(f"Uspesan login sa {mail} i {sifra}!!!!")
    else:
        print("Neuspesan login!")

#loginTest("cmcnally0@usa.gov", "sKwkqGD4RwN")

for element in MockData.TEST_DATA2:
    loginTest(element["email"],element["sifra"])
