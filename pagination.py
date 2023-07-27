from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_page_source(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    page_source = driver.page_source
    return page_source


def get_soup(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup


def get_next_page(soup):
    pagination = soup.find('div', class_='pagination-desktop')
    no_next = pagination.find('span', class_='next_page disabled')
    if not no_next:
        return 'https://www.nepalicars.com' + str(soup.find('a', class_='next_page')['href'])
    else:
        return


def get_list_links(url):
    url_list = []
    while True:
        url_list.append(url)
        page = get_page_source(url)
        page_soup = get_soup(page)
        link = get_next_page(page_soup)
        if not link:
            break
        url = link
    return url_list


