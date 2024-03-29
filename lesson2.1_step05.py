from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer.form-control")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector(".form-check-custom > .form-check-label")
    option1.click()

    option2 = browser.find_element_by_css_selector(".form-radio-custom > .form-check-label")
    option2.click()

    button = browser.find_element_by_css_selector(".container .btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.quit()


