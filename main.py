from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import excel
load_dotenv()
USEREMAIL = os.getenv("USEREMAIL")
PASSWORD = os.getenv("PASSWORD")
EXCEL_PATH = os.getenv("EXCEL_PATH")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get("http://127.0.0.1:5501/webFront/login/login.html")
browser.find_element('xpath', '//*[@id="email"]').send_keys(USEREMAIL)
browser.find_element('xpath', '//*[@id="password"]').send_keys(PASSWORD)
browser.find_element('xpath', '//*[@id="submit_button"]').click()

tasks = excel.readExcel(EXCEL_PATH)
browser.get('http://127.0.0.1:5501/webFront/inicial/inicial.html')

for task in tasks:
    browser.find_element('xpath', '//*[@id="adicionar"]').click()
    browser.find_element('xpath', '//*[@id="titulo"]').send_keys(task[0])
    browser.find_element('xpath', '//*[@id="data"]').send_keys(task[1])
    browser.find_element('xpath', '//*[@id="button_criar"]').click()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    browser.switch_to.alert.accept()