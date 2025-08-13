from pages.login_page import LoginPage
from utils import data

def test_login_sucesso(driver):
    driver.get(data.BASE_URL)
    login_page = LoginPage(driver)

    login_page.enter_username(data.USERNAME)
    login_page.enter_password(data.PASSWORD)
    login_page.click_login()

    assert "Página Inicial" in driver.title
