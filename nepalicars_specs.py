from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from nepalicars import get_urls


url = 'https://www.nepalicars.com/en/vehicle_listings/ad-hyundai-i10-bagmati-kathmandu-4303'
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
page = driver.page_source
driver.quit()

soup = BeautifulSoup(page, 'html.parser')
print(soup.find_all('div', class_='ad-about'))
def main():
    urls = get_urls()
    return urls


if __name__ == '__main__':
    print(main())