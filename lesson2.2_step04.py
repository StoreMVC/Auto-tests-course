from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum(a, b):
    return str(a + b)

try:
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing'; alert('Robots at work');")

finally:
    time.sleep(10)
    browser.quit()


