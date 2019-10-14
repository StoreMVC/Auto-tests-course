from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button1 = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card-body #price"), "$100")
        )
    button2 = browser.find_element_by_css_selector("#book.btn")
    button2.click()

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer.form-control")
    input1.send_keys(y)

    button3 = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    button3.click()
    
    
finally:
    time.sleep(10)
    browser.quit()
