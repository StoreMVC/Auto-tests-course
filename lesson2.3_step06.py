from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer.form-control")
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector(".btn.btn-primary")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()


