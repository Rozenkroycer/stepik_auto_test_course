from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

fake = Faker()
fake_name = fake.name()
fake_last_name = fake.last_name()
fake_city = fake.city()
fake_country = fake.country()

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
try:
    browser.get(link)

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys(fake_name)
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys(fake_last_name)
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys(fake_city)
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys(fake_country)
    button = browser.find_element(By.XPATH, "//*[@type='submit']")
    button.click()
    time.sleep(30)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла

