import requests
import config
from bs4 import BeautifulSoup
import os.path
import json
import pickle


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
    
with open('groups/allgroups.pkl', 'wb') as file:
    pickle.dump(group_numbers, file)

if __name__ == '__main__':
    print(group_numbers)