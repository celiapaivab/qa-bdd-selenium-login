from behave import given, when, then
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.data import USERNAME, PASSWORD

@given("I am on the login page")
def open_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when("I enter valid credentials")
def add_credentials(context):
    context.login_page.enter_username(USERNAME)
    context.login_page.enter_password(PASSWORD)

@when("I click the login button")
def click_button(context):
    context.login_page.click_login()

@then("I should be redirected to the secure area")
def open_secure_area(context):
    context.secure_page = SecureAreaPage(context.driver)
    tittle = context.secure_page.get_page_tittle()
    assert "Secure Area" in tittle

@then("I should see a success message")
def check_message(context):
    message = context.secure_page.get_flash_message()
    assert "You logged into a secure area!" in message