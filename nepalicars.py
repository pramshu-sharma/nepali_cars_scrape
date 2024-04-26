from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from pagination import get_list_links

urls = get_list_links('https://www.nepalicars.com/en/vehicle_listings?page=1')
spec_urls = []
for page in urls:
    url = page
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
        spec_urls.append(link_prefix + str(link['href']))
    print(f'Pages Completed: {page}')

df_links = pd.DataFrame(spec_urls, columns=['urls'])
df_links.to_csv('nepalicars_all_links.csv', index=False)

# test comment



