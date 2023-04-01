from behave import *
from features.environment import before_all
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@given('we have navigated to the url')
def step_impl(context):
    driver.get('https://qxf2.com/selenium-tutorial-main')  
    driver.maximize_window

@when('we check the title')
def step_impl(context):
    if driver.title.istitle:
         print("Title is present")
    else:
         print ("Title not found")

@then('we verify the title of the page')
def step_impl(context):
    assert(driver.title == 'Qxf2 Services: Selenium training main')

@given(u'we enter name in the name field')
def step_impl(context):
    enter_name = driver.find_element(By.NAME, 'name')
    enter_name.send_keys('Ajitava')

@when(u'we enter email in the email field')
def step_impl(context):
    enter_email = driver.find_element(By.NAME, 'email')
    enter_email.send_keys('ajitava@deb.com')

@then(u'we enter phone number in the phone number field')
def step_impl(context):
    enter_phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    enter_phone.send_keys('123456789')

@when(u'we click the drop down')
def step_impl(context):
    click_dropdown = driver.find_element(By.CSS_SELECTOR, "button[type='button']")
    click_dropdown.click

@when(u'we select male from drop down')
def step_impl(context):
    select_option = driver.find_element(By.XPATH, "//a[text()='Male']")    
    select_option.click

@when(u'we check the checkbox')
def step_impl(context):
    select_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    select_checkbox.click

@when(u'we click the click me button')
def step_impl(context):
    select_button = driver.find_element(By.XPATH, "//button[text()='Click me!']")
    select_button.click
