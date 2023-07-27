from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd


def get_urls():
    urls = []
    for page in range(1, 2):
        url = f'https://www.nepalicars.com/buy-cars?page={page}'

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')
        link_prefix = 'https://www.nepalicars.com'
        links = soup.find_all('a', class_='common-ad-card', href=True)

        for link in links:
            urls.append(link_prefix + str(link['href']))
        print(f'Pages Completed: {page}')

        dataframe_urls = pd.DataFrame({'url': urls})
        return dataframe_urls