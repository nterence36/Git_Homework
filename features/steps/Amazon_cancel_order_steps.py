from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open the amazon help link')
def Open_help_link(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('type in cancel order on the search bar')
def Type_cancel_order(context):
    search = context.driver.find_element(By.XPATH, "//input[@type='search']").send_keys('cancel orders', Keys.ENTER)



