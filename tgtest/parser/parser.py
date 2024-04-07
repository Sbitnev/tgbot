import requests
import config
from bs4 import BeautifulSoup


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain='https://itmo.ru/ru/schedule/0/', 
        week=week, 
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def get_schedule(web_page):
    soup = BeautifulSoup(web_page, "html.parser")

    # Получаем таблицу с расписанием на понедельник
    schedule_table = soup.find("table", attrs={"id": "1day"})

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list

page = get_page('K34202', '1')
times_lst, locations_lst, lessons_lst = get_schedule(page)

print(times_lst)
print(locations_lst)
print(lessons_lst)
