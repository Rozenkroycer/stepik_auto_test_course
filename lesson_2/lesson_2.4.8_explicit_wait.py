from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не будет 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    if price is True:
        book_button = browser.find_element(By.ID, "book")
        book_button.click()

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)

        answer_input = browser.find_element(By.ID, "answer")
        answer_input.send_keys(y)

        submit_button = browser.find_element(By.ID, "solve")
        submit_button.click()

    else:
        print("Остаемся дома")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()