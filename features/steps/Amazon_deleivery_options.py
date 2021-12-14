from selenium.webdriver.common.by import By
from behave import given, when, then

Delivery_options = (By.CSS_SELECTOR, "div#prime-benefit-module-content-delivery-item h2")

@given('Open amazon prime page')
def Open_amazon_page(context):
    Context.driver.get('https://www.amazon.com/amazonprime/')

@then('verify that user sees three delivery options')
def Delivery_options(context):
    delivery_ways = context.driver.find_elements(*Delivery_options)
    assert len(delivery_ways) == 3, f'Expected 3 delivery ways, but got {len(delivery_ways)}'