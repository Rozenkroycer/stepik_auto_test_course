from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    x = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    y = int(num2.text)
    sum = x + y
    print(sum)

    # Вводим рассчитанное значение в поле
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()