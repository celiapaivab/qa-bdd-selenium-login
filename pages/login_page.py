from selenium.webdriver.common.by import By
from utils.data import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")
        self.error_message = (By.CSS_SELECTOR, ".flash.error")
        self.page_tittle = (By.TAG_NAME, "h2")

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

    def get_error_message(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_message))
        return self.driver.find_element(*self.error_message).text

    def get_page_tittle(self):
        return self.driver.find_element(*self.page_tittle).text

    def login_valid_user(self):
        self.enter_username(USERNAME)
        self.enter_password(PASSWORD)
        self.click_login()