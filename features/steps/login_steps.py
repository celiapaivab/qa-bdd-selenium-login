from behave import given, when, then
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.data import *

@given("I am on the login page")
def open_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when("I enter valid credentials")
def add_credentials(context):
    context.login_page.enter_username(USERNAME)
    context.login_page.enter_password(PASSWORD)

@when("I enter invalid username")
def add_invalid_username(context):
    context.login_page.enter_username(INVALID_USERNAME)
    context.login_page.enter_password(PASSWORD)

@when("I enter invalid password")
def add_invalid_password(context):
    context.login_page.enter_username(USERNAME)
    context.login_page.enter_password(INVALID_PASSWORD)

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

@then("I should see an username error message")
def check_username_error(context):
    message = context.login_page.get_error_message()
    assert "Your username is invalid!" in message

@then("I should see a password error message")
def check_password_error(context):
    message = context.login_page.get_error_message()
    assert "Your password is invalid!" in message