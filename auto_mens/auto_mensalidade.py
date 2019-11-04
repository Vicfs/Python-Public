from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# initializing the webdriver along with geckodriver.exe path.
browser = webdriver.Firefox(executable_path='C:\\gecko\\geckodriver.exe')
browser.get('https://www3.mackenzie.br/tia/')

# opening json and sending login/password data.
with open('creds.json', 'r') as pfile:
    credentials = json.load(pfile)
matric = browser.find_element_by_name('alumat')
matric.send_keys('', credentials['login'])
passw = browser.find_element_by_name('pass')
passw.send_keys('', credentials['password'])
pfile.close()

# entering intended page.
browser.find_element_by_xpath("//select[@name='unidade']/option[text()='Universidade Presbiteriana Mackenzie (campus Higienópolis)']").click()
browser.find_element_by_css_selector('.btn-block').click()

# waiting for the element to be clickable and downloading the file.
wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'sit.')))
browser.find_element_by_partial_link_text('sit.').click()
browser.find_element_by_class_name('link10').click()
browser.close()
