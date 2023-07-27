from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
'''


ad create date
views
all specs
seller name
seller contact
'''



url = 'https://www.nepalicars.com/en/vehicle_listings/ad-maruti-wagon-r-bagmati-bhaktapur-4326'
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')
title = soup.find('div', class_='ad-title').find('h2').text
location = soup.find('div', class_='ad-title').find('span').text
npr_price = soup.find('div', class_='ad-price').find('span', class_='price').text
usd_price = soup.find('div', class_='accordion-sub-card free').find('span', class_='price').text
create_date = soup.find('div', class_='ad-created-border').find('strong').text


