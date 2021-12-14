from selenium.webdriver.common.by import By
from behave import given, when, then

Cart = (By.ID, 'nav-cart-count')

@when('Search for shoes')
def search_zin(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shoes')

@when('click first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH, "//a[.//span[@class='a-price']]").click()

@when('click on add to card button')
def add_to_cart(context):
    context.driver.find.element(By.CSS_SELECTOR, "input#add-to-cart-button.a-button-input").click()

@then('verify cart has 1 item(s)')
def Verify_item_is_added(context):
    Actual = context.driver.find_element(*Cart).text
    Expected = '1'

    assert Actual == Expected, f'Expected {Expected}, but we got {Actual}'

    print('Test case pass')