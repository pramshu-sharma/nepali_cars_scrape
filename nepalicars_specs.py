from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_time = time.time()
with open('C:/Users/Pramshu/PycharmProjects/NepaliCars/nepalicars_all_links.csv') as file:
    csv_reader = csv.reader(file)
    for rows in csv_reader:
        url = rows[0]
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')

        title = soup.find('div', class_='ad-title').find('h2').text
        location = soup.find('div', class_='ad-title').find('span').text
        try:
            npr_price = soup.find('div', class_='ad-price').find('span', class_='price').text
            usd_price = soup.find('div', class_='accordion-sub-card free').find('span', class_='price').text
        except AttributeError:
            npr_price = soup.find('div', class_='ad-price').text
            usd_price = soup.find('div', class_='ad-price').text
        create_date = soup.find('div', class_='ad-created-border').find('strong').text
        views = soup.find_all('div', class_='ad-info-block')[2].find('strong').text
        try:
            seller = soup.find('div', class_='profile-data').find('h5').text
            seller_contact = soup.find('div', class_='phone-wrapper-call-seller').find('span').text
        except AttributeError:
            seller, seller_contact = 'N/A', 'N/A'

        # vehicle_properties = soup.find('div', class_='vehicle-properties').find_all('div', class_='prop')
        print(title, location, npr_price, usd_price, create_date, views, seller, seller_contact, rows[0])
end_time = time.time()
print(f'Time Taken: {round(end_time - start_time, 2)} seconds')
