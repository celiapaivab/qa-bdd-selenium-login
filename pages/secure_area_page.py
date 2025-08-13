from selenium.webdriver.common.by import By

class SecureAreaPage:
    def __init__(self, driver):
        self.driver = driver
        self.flash_message = (By.ID, "flash")
        self.page_tittle = (By.TAG_NAME, "h2")
        self.logout_button = (By.CSS_SELECTOR, "a.button")

    def get_flash_message(self):
        return self.driver.find_element(*self.flash_message).text

    def get_page_tittle(self):
        return self.driver.find_element(*self.page_tittle).text

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()