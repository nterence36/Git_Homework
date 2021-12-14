from selenium.webdriver.common.by import By
from behave import given, when, then

Hex = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a")
@given('Open best seller page')
def Open_Best_seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify you see five links')
def Best_seller_links_check(context):
    Actual = context.driver.find_elements(*Hex)

    assert len(Actual) == 5, f' expected 5 but got {len(Actual)}'

