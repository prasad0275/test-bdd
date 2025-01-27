from behave import given, when, then
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

@given(u'user is on the login page')
def step_impl(context):
    context.driver = Chrome()
    context.driver.get("https://www.saucedemo.com/")


@when('user enters username "{username}" and password "{password}" and click login')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, 'user-name').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'login-button').click()


@then(u'verify the login process')
def step_impl(context):
    try:
        title = context.driver.find_element(By.XPATH, '//div[@class="app_logo"]').text
        assert "Swag Labs" in title, "Test Passed"
    except: 
        context.driver.close()
        assert False, "Test Failed"

@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    