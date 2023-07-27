from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.nepalicars.com/en/vehicle_listings/ad-maruti-wagon-r-bagmati-bhaktapur-4326'
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')
prop = soup.find('div', class_='vehicle-properties').find_all('span')
print(prop)

