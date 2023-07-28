from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

start_time = time.time()
with open('C:/Users/Pramshu/PycharmProjects/NepaliCars/nepalicars_all_links.csv') as file:
    csv_reader = csv.reader(file)
    car_details_list = []
    car_count = 1
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
            price_npr = soup.find('div', class_='ad-price').find('span', class_='price').text
            price_usd = soup.find('div', class_='accordion-sub-card free').find('span', class_='price').text
        except AttributeError:
            price_npr = soup.find('div', class_='ad-price').text
            price_usd = soup.find('div', class_='ad-price').text
        create_date = soup.find('div', class_='ad-created-border').find('strong').text
        views = soup.find_all('div', class_='ad-info-block')[2].find('strong').text
        try:
            seller = soup.find('div', class_='profile-data').find('h5').text
            seller_contact = soup.find('div', class_='phone-wrapper-call-seller').find('span').text
        except AttributeError:
            seller, seller_contact = 'N/A', 'N/A'
        car_details = \
            {
                'URL': rows[0],
                'Title': title,
                'Location': location,
                'Price (NPR)': price_npr.replace(',', ''),
                'Price (USD)': price_usd.replace(',', ''),
                'Ad Create Date': create_date,
                'Ad Views': views,
                'Seller': seller,
                'Contact Number': seller_contact
            }
        vehicle_properties = soup.find('div', class_='vehicle-properties').find_all('div', class_='prop')
        for props in vehicle_properties:
            search_span = props.find('span')
            key = search_span.text
            value = search_span.find_next('span').text
            car_details[key] = value
        car_details_list.append(car_details)
        end_time = time.time()
        print(f'Details Scrapped: {car_count}, URL: {rows[0]}, Time Taken (Total): {round((end_time - start_time)/60, 2)} minutes')
        car_count += 1

df = pd.DataFrame(car_details_list, index=None)
df.to_csv('nepalicars_car_details.csv', index=False)
