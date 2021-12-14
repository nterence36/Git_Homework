from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Search result have table')
def verify_search_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_result = '"table"'
    assert actual_result == expected_result, f'Error, actual {actual_result} did not match our expected {expected_result}'