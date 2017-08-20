# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import re 
import urllib2
import urllib 
import cookielib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 

def single_page_scrape(page,file_adress):	 
 
	soup = BeautifulSoup(page.content, 'lxml')

	df = {  
	'ADDR_1': [],
	'ADDR_2': [],
	'ADDR_3': [],
	'ADDR_4': [],
	'ADDR_5': [],
	'TITTLE':[],
	'FULLNAME':[],
	'TELEPHONE':[],
	'EMAIL':[],
	'PRI_ORG':[],		
	}

	# find the main organization 
	main_org = soup.find("td",{"class":"ba"}).contents[1]
	# find the main address 
	try: 
		address_1 = soup.find("td",{"class":"sm"}).findNext('td').text.encode('utf-8')
	except:
		address_1 = ''
 
	# get all tables in selected part 
	get_data = soup.find_all("table")
	
	# not include the first table
	for item in get_data[1:]: 
	
	# arrays must all be same length
		df['PRI_ORG'].append(main_org)
		df['ADDR_1'].append(address_1)

		try:
			title = item.find("td",{"class":"ID72"}).contents[0].encode('utf-8').strip()
		except:
			title = ''
		df['TITTLE'].append(title)

		try:
			full_name = item.find("td",{"class":"ID72"}).find("a").text.replace('&nbsp;', '')
		except:
			full_name = ''
		df['FULLNAME'].append(full_name)

		try:
			tele = item.find("td",{"class":"TD24"}).text
		except:
			tele = ''
		df['TELEPHONE'].append(tele)

		try:
			email = item.find("td",{"class":"me"}).find("a").text
		except:
			email = ''
		df['EMAIL'].append(email)

	df = pd.DataFrame(df)
	df = df[[
 		'PRI_ORG',		
 		'ADDR_1',
 		'ADDR_2',
		'ADDR_3',
		'ADDR_4',
		'ADDR_5',
		'FULLNAME',
		'TITTLE',
		'EMAIL',
		'TELEPHONE',
		]]
 	df.to_csv(file_adresss+ main_org +'.csv', encoding='utf-16',index=False, header=None, sep='\t')


