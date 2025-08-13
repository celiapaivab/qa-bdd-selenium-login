from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_chrome_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--user-data-dir=/tmp/temp-chrome-profile")
    return webdriver.Chrome(options=options)

def before_scenario(context, scenario):
    context.driver = create_chrome_driver()

def after_scenario(context, scenario):
    context.driver.quit()
