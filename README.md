This distributed web scraping project is made by **Python2.7**. 
High flexible to manage and extract structured data from webpages.
## Architecture 
![alt text](https://github.com/jieren123/Web_Crawler_Scraper/blob/master/web_crawler_system.png "Web Crawler-Scraper System")

## Main Features 
- Automation: Autologin is to make it easier for web spider to crawl websites that require authenticaion. 
  -  Automiatically find login fields and can handle login that requires dynamic CSRF token. 
  -  Provide it with one single account credentials and persisted cookies for the duration the session and can be recalled in other            activities. 
  -  Obtain form requests to submit from your own spider and args for spider to sumbit. No http requests and dependencies are made.

- Dynamics: 
  -  Visualize result when you make selection in Ajex table and monitor it 
  -  Dynamically visit ASP.NET pages on and scrape content from it 
  -  Access to AJAX pagination for the next page automatically until the end. 

- Storage: 
  - Uses DataFrame to store crawled website data based on classification and creates the DataFrame automatically the first time the           spider is running.
  - Optionally save large webpages to disk by mapreduce method.

## Main difference from Scrapy 
- Easy to maintain and extend 
- Less Memory leak

## Requirement 
- BeautifulSoup4 
- python 2.7
- Selenium
- pandas
- numpy
- re 

## Main files 
- auto-login.py: login with cookies
- get-querystring.py: get guery-string parameter; AJAX pagination
- url-generator: generate url address
- single-page.py: Scape with item on a singe page and save it into local csv file.
- multiple-files.py: Manipulate multiple large database files
- file-clear.py : Deal with missing value; Convert unstructed data into structured data


