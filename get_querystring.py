from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd 
import time
	
def part_select(browser,select_page):
	# After login, get wanted page
	browser.get(select_page)

	# waiting for 5 second to load web page
	time.sleep(5)

	# select the organizaiotns buttion 
	organizaiotns_buttion = "img[onclick='SwtichToTab(4)']"
	browser.find_element_by_css_selector(organizaiotns_buttion).click()
	time.sleep(2)
		
	# select wanted organization(MAIN_PART TO MAKE SELECTION)

	sele_org = "img[value='20464']"
	browser.find_element_by_css_selector(sele_org).click()
	time.sleep(3)

	sele_org = "img[value='16143']"
	browser.find_element_by_css_selector(sele_org).click()
	time.sleep(3)

	sele_org = "img[value='18761']"
	browser.find_element_by_css_selector(sele_org).click()
	time.sleep(3)

	sele_org = "img[value='20465']"
	browser.find_element_by_css_selector(sele_org).click()
	time.sleep(3)

	sele_org = "img[value='16505']"
	browser.find_element_by_css_selector(sele_org).click()
	time.sleep(3)

	# go to next page(MAIN_PART TO MAKE SELECTION) 
	next_buttion = "div[title='Next Results (101-200 of 216)']"
	browser.find_element_by_css_selector(next_buttion).click()
	time.sleep(3)

	# go to view result buttion 
	#viewresult_buttion = "img[onclick='SwtichSrchToView();']"
	viewresult_buttion = "img[id='idTabViewSrch']"
	browser.find_element_by_css_selector(viewresult_buttion).click()
	time.sleep(3)

	# view the organization result
	vieworgresult_bution = "a[href='javascript:GridSetViewWhat(1);']"
	browser.find_element_by_css_selector(vieworgresult_bution).click()
	time.sleep(3)

	return browser   	
 

# Using selenium to Scrape ASP.NET Pages with AJAX Pagination 
def get_query(browser, page_no):
# creat urls to store urs 
	df_url= {
		"urls":[]
	}

	# browser with url address 
	page = 0
	while page <page_no:
		# get url_address by BeautifulSoup
		soup = BeautifulSoup(browser.page_source, 'lxml')
		url_pool = soup.find("table",{"id":"idTblGridData"})
		url_adds = url_pool.find_all("a", href = True)
		for url_add in url_adds:
			try:
				url_js = url_add["href"]
			except:
				url_js = ""
			df_url["urls"].append(url_js)

		
		# if we reach the last page, we can't find the next buttion.
		page = page+1
 
		try:
			next_page = "//*[@id='idBvdGrid']/tbody/tr[3]/td/table/tbody/tr/td[2]/a[5]"
			browser.find_element_by_xpath(next_page).click()
		except:
			next_page = "//*[@id='idBvdGrid']/tbody/tr[3]/td/table/tbody/tr/td[2]/a[7]"
			browser.find_element_by_xpath(next_page).click()

		time.sleep(10)
		
	df_query = pd.DataFrame(df_url)
	df_query.to_csv('/Users/JieREN/Desktop/ihope/web_scraping/query.csv', index=False, header="urls")


