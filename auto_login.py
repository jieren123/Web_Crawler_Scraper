import pickle
import requests
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# When you login the website through selenium, you have to stop for seconds
def login(path,username, password):
	browser = webdriver.Chrome()
	browser.get(path)

	time.sleep(3)
 
	emailFieldID = "input[tabindex='1']" 
	passFieldID = "input[tabindex='2']"
	loginButton = "submit"

	emailFieldElement = browser.find_element_by_css_selector(emailFieldID)
	passFieldElement = browser.find_element_by_css_selector(passFieldID)
	loginButtonElement = browser.find_element_by_name(loginButton)
 
	emailFieldElement.send_keys(username)
	passFieldElement.send_keys(password)
	loginButtonElement.click()
 
	return browser    

# keep cookie
def keep_cookies(browser):

	# to get cookie from browser
	request = requests.Session()
	headers = {
		"User-Agent":
			"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
			"(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	}
	request.headers.update(headers)
	cookies = browser.get_cookies()

	# save the current cookies locally 
	for cookie in cookies:
		request.cookies.set(cookie['name'], cookie['value'])
	return request


