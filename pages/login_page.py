from selenium.webdriver.common.by import By
from utils.data import *

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")
        self.flash_message = (By.ID, "flash")

    def load(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_valid_user(self):
        self.enter_username(USERNAME)
        self.enter_password(PASSWORD)
        self.click_login()