import requests
import config
from bs4 import BeautifulSoup
import os.path
import json


url = 'https://itmo.ru/ru/schedule/raspisanie_zanyatiy.htm'
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
group_links = soup.find_all('div', class_='groups')#.find_all('a')

arr = []

for a in group_links:
    arr += a.find_all('a')

# Извлекаем текст из каждой ссылки
group_numbers = [link.text for link in arr]
    
if __name__ == '__main__':
    print(group_numbers)