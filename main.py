from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
import time
import os

# Variables
chromedriver_path = os.path.expandvars("%HOMEPATH%\\.cache\\selenium\\chromedriver\\win64\\133.0.6943.126\\chromedriver.exe")
chrome_path = os.path.expandvars("%HOMEPATH%\\.cache\\selenium\\chrome\\win64\\133.0.6859.0\\chrome.exe")

# Set up options
options = webdriver.ChromeOptions()
service = Service(chromedriver_path) # Chromedriver path
options.binary_location = chrome_path
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
user_data_dir = os.path.abspath("./data")
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument("start-maximized")
options.add_argument("--headless")

# Driver instance injection
driver = webdriver.Chrome(service=service, options=options)

# Stealth settings
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

def keydrop_daily_case():
    try:
        driver.get("https://key-drop.com/en/daily-case")
        print('Keydrop website accessed.')
        time.sleep(10)
        daily_free = driver.find_element(By.XPATH, '//*[@id="dailyCase-root"]/div[1]/ul/li[1]/button')
        print('Daily Free obtained.')
        assert daily_free.click()
        time.sleep(4)
    finally:
        print('Closing webdriver...')
        driver.quit()

def first_time_login():
    try:
        driver.get("https://store.steampowered.com/login/")
        # The user has 10 seconds to log-in.
        time.sleep(10)
        driver.get("https://key-drop.com/en/daily-case")
    finally:
        driver.quit()

# Execute one of the functions:
keydrop_daily_case()
first_time_login()