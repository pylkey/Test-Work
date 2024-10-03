import requests, tldextract
from bs4 import BeautifulSoup
from collections import namedtuple
from typing import Union


parse_info=[
    {'domain':'mvideo.ru', 'title':'product-title', 'price':'price-micro', 'desc':'product-description'},
    {'domain':'yandex.ru', 'title':'title', 'price':'price', 'desc':'description'},
    {'domain':'dns-shop.ru', 'title':'product-title', 'price':'price', 'desc':'product-description'},
]

headers='user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'


def get_site_name(url:str)->str:
    extracted = tldextract.extract(url)
    return f"{extracted.registered_domain}"


def parse(url:str, info:dict)->Union[namedtuple, None]:
    response = requests.get(url, headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_element = soup.find('h1', class_=info['title'])
        title = title_element.text.strip() if title_element else "Название не найдено"
        
        price_element = soup.find('span', class_=info['price'])
        price = price_element.text.strip() if price_element else "Цена не найдена"
        
        description_element = soup.find('div', class_=info['desc'])
        description = description_element.text.strip() if description_element else "Описание не найдено"
        
        Product = namedtuple('Product', [title, price, description, url])

        return Product
    else:
        return f"Ошибка при запросе страницы: {response.status_code}"
    

def do_parse(url):
    for info in parse_info:
        if info['domain'] == get_site_name(url):
            parse(url,info)
        else:
            parse(url, {'title':'title', 'price':'price', 'desc':'description'})
    

