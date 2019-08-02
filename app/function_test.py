from selenium import webdriver
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER = os.path.join(ROOT_DIR, '.utils')

browser = webdriver.Chrome(CHROME_DRIVER+'/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
