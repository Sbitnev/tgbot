import requests
import config
from bs4 import BeautifulSoup
import os.path
import json

def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain='https://itmo.ru/ru/schedule/0/', 
        week=week, 
        group=group)
    response = requests.get(url)
    if response.status_code == 200:
        print("Ссылка указана правильно и страница доступна!")
    else:
        print("Что-то не так с указанной ссылкой.")
    web_page = response.text
    return web_page


def get_schedule(web_page, day=1):
    soup = BeautifulSoup(web_page, "html.parser")
    
    if 'Расписание не найдено' in web_page:
        return 'error', 'error', 'error'

    elif soup.find("table", attrs={"id": str(day) + "day"}):
        
        # Получаем таблицу с расписанием на понедельник
        schedule_table = soup.find("table", attrs={"id": str(day) + "day"})

        # Время проведения занятий
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
        times_list = [time.span.text for time in times_list]

        # Место проведения занятий
        locations_list = schedule_table.find_all("td", attrs={"class": "room"})
        locations_list = [room.span.text for room in locations_list]

        # Название дисциплин и имена преподавателей
        lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
        lessons_list = [lesson.text.split('                                                                ') for lesson in lessons_list]
        lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]
        lessons_list = [string.replace('\n', '') for string in lessons_list]
        lessons_list = [string.replace('     ', ' ') for string in lessons_list]
        lessons_list = [string.strip() for string in lessons_list]

        return times_list, locations_list, lessons_list
    
    else:
        return None, None, None
     

def dayjson(day, times_lst, locations_lst, lessons_lst):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    lesson = [{ 'time': v, 'addr': a, 'info': i } for v, a, i in zip(times_lst, locations_lst, lessons_lst)]
    return {days[day] : lesson}

def get_schedulejson(group):
    week = ['odd', 'even']
    schedule = {}
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(2):
        page = get_page(group, str(i+1))
        arr = {}
        for a in range(7):
            times_lst, locations_lst, lessons_lst = get_schedule(page, a+1)
            if times_lst:
                arr.update(dayjson(a, times_lst, locations_lst, lessons_lst))
            else:
                arr.update({days[a] : 'No lessons'})
        schedule[week[i]] = arr
    
    return schedule


def get_groupschedule(group):
    group = group.upper()
    if not os.path.exists('groups/'+str(group)+'.json'):
            web_page = get_page(group)
            if 'Расписание не найдено' in web_page:
                print('Group does not exist')
                return None
            else:
                with open('groups/'+str(group)+'.json', 'w') as json_file:
                    json.dump(get_schedulejson(str(group)), json_file, indent=4, ensure_ascii=False)
                    print('File created')
                    return 1
    else:
        print('File exists')
        return 1

# if get_groupschedule('M34t4r001'):
#     print('wow')
        

# i = 1
# group = 'K34202'
# schedule = {}
# week = ['odd', 'even']
# page = get_page(group, str(i+1))
# arr = []
# for a in range(7):
#     times_lst, locations_lst, lessons_lst = get_schedule(page, a+1)
#     arr += dayjson(a, times_lst, locations_lst, lessons_lst)
# schedule[week[i]] = arr

# page = get_page('K34202', '1')
# times_lst, locations_lst, lessons_lst = get_schedule(page, 3)

# with open('parser/example.txt', 'w') as file:
#     file.write(page)

# print(times_lst)
# print(locations_lst)
# print(lessons_lst)

# # days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# lesson = [{ 'time': v, 'addr': a, 'info': i } for v, a, i in zip(times_lst, locations_lst, lessons_lst)]
# print(lesson)