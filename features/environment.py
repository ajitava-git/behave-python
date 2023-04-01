from selenium import webdriver

def before_all(driver):
    driver = webdriver.Chrome()
