from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify result have "Cancel Items or Orders"')
def Verify_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = 'Cancel Items or Orders'

    assert actual_result == expected_result, f'Expected {expected_result}, but we got {actual_result}'

    print('Test case pass')
