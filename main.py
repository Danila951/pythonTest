from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def testSearch():
    driver = webdriver.Chrome('C:/Users/User/PycharmProjects/pythonTest/venv/chromedriver')
    driver.get("https://www.kupibilet.ru/")
    time.sleep(3)
    inputWhere = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[1]/div[3]/div/div[1]/div[3]/div[1]/input")
    inputWhere.send_keys("Сочи")
    time.sleep(2)
    menu = driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1']/ul")
    menu.click()
    time.sleep(2)
    buttonSearch = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[1]/div[3]/div/div[2]/div[2]/button")
    buttonSearch.click()
    time.sleep(2)
    dateOut = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[1]/input")
    if dateOut.get_attribute('placeholder') == "Укажите дату":
        print("сработало")
    else:
        print("Не сработало")
    time.sleep(1)
    driver.quit()

def testSearch2():
    driver = webdriver.Chrome('C:/Users/User/PycharmProjects/pythonTest/venv/chromedriver')
    driver.get("https://www.kupibilet.ru/")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    inputEmail = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[6]/div/div/div/div/form/div[1]/div/div/div/input")
    inputEmail.send_keys("123456")
    time.sleep(2)
    buttonSearche = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[6]/div/div/div/div/form/div[1]/div/button")
    buttonSearche.click()
    time.sleep(2)
    out2 = driver.find_element(By.XPATH, "//*[@id='app-wrap']/div[2]/div[6]/div/div/div/div/form/div[1]/div/div/div/span")
    if out2.text == "Неверный формат электронной почты":
        print("сработало")
    else:
        print("Не сработало")
    driver.quit()


testSearch2()