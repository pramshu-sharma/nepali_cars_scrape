from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.nepalicars.com/en/ads/ad-hyundai-i10-bagmati-kathmandu-4286'
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
views = soup.find_all('div', class_='ad-info-block')[2].find('strong').text
seller = soup.find('div', class_='profile-data').find('h5').text
seller_contact = soup.find('div', class_='phone-wrapper-call-seller').find('span').text


vehicle_properties = soup.find('div', class_='vehicle-properties').find_all('div', class_='prop')
print(seller_contact)




