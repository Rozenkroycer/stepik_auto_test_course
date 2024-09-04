from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    image = browser.find_element(By.ID, "treasure")
    x = image.get_attribute("valuex")
    y = calc(x)

    # Вводим рассчитанное значение в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем на чек-бокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()


    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_radiobutton.click()

    submit_button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()