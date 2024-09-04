from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstname_input = browser.find_element(By.NAME, "firstname")
    firstname_input.send_keys("Ivan")

    lastname_input = browser.find_element(By.NAME, "lastname")
    lastname_input.send_keys("Ivanov")

    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("test@test.com")

    file_input = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()