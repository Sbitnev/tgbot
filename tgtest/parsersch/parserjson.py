import requests
import config
from bs4 import BeautifulSoup
import os.path
import json

allg = ['K3120', 'K3121', 'K3122', 'K3123', 'K3139', 'K3140', 'K3141', 'MC1 1', 'MC1 1.1', 'P3106', 'P3107', 'P3108', 'P3109', 'P3110', 'P3111', 'P3112', 'P3113', 'P3114', 'P3115', 'P3116', 'P3117', 'P3118', 'P3119', 'P3120', 'P3121', 'P3122', 'P3123', 'P3124', 'P3125', 'P3130', 'P3131', 'P3132', 'L3216', 'L3217', 'M3200', 'M3201', 'M3202', 'M3203', 'M3204', 'M3205', 'M3206', 'M3207', 'M3208', 'M3209', 'M3210', 'M3211', 'M3212', 'M3213', 'M3214', 'M3215', 'M3216', 'M3217', 'M3218', 'M3219', 'M3220D', 'M3221D', 'M3231', 'M3232', 'M3233', 'M3234', 'M3235', 'M3236', 'M3237', 'M3238', 'M3239', 'MC2 1', 'MC2 1.1', 'O3243', 'O3244', 'U3279D', 'U3280D', 'V3202', 'V3203', 'Z3243', 'Z3244', 'B33001', 'B33002', 'B33003', 'D33101', 'H33212', 'H33232', 'K33201', 'K33202', 'K33211', 'K33212', 'K33391', 'K33392', 'K33401', 'K33402', 'K33421', 'K33422', 'L33161', 'L33162', 'L33181', 'L33182', 'M33001', 'M33011', 'M33021', 'M33031', 'M33051', 'M33061', 'M33071', 'M33081', 'M33091', 'M33101', 'M33111', 'M33121', 'M33321', 'M33331', 'M33341', 'M33351', 'M33361', 'M33371', 'M33381', 'M33391', 'N33451', 'N33452', 'N33453', 'N33461', 'N33471', 'N33481', 'N33491', 'N33501', 'N33511', 'N33521', 'N33522', 'N33523', 'N33531', 'N33532', 'O33431', 'O33432', 'O33442', 'P3304C', 'P33081', 'P33082', 'P33091', 'P33092', 'P33101', 'P33102', 'P33111', 'P33121', 'P33131', 'P33141', 'P33151', 'P33201', 'P33202', 'P33211', 'P33212', 'P33222', 'P33232', 'P33301', 'P33302', 'P33311', 'P33312', 'P33661', 'P33662', 'P33663', 'P33664', 'P33691', 'P33692', 'P33693', 'P33694', 'R33351', 'R33352', 'R33353', 'R33362', 'R33372', 'R33401', 'R33402', 'R33403', 'R33412', 'R33413', 'R33423', 'R3342C', 'R33801', 'R33802', 'R33811', 'R33812', 'R3398C', 'T33301', 'T33302', 'T33303', 'T33304', 'T33305', 'T33311', 'T33321', 'U3310D', 'U3378D', 'V33021', 'V33022', 'V33023', 'V33031', 'W33051', 'W33052', 'W33602', 'Z33431', 'Z33432', 'Z33433', 'Z33434', 'B34001', 'B34002', 'B34003', 'B34222', 'B34223', 'B34232', 'B34233', 'D34101', 'K34201', 'K34202', 'K34211', 'K34212', 'K34401', 'K34402', 'K34412', 'K34421', 'K34422', 'L34161', 'L34162', 'L34181', 'L34182', 'M34001', 'M34011', 'M34021', 'M34031', 'M34041', 'M34051', 'M34061', 'M34071', 'M34081', 'M34091', 'M34112', 'M34341', 'M34351', 'M34361', 'M34371', 'M34381', 'M34391', 'N34461', 'N34462', 'N34463', 'N34471', 'N34481', 'N34491', 'N34501', 'N34511', 'N34521', 'N34523', 'N34531', 'N34532', 'P3404C', 'P34101', 'P34102', 'P34111', 'P34121', 'P34131', 'P34201', 'P34202', 'P34211', 'P34212', 'P34222', 'P34301', 'P34302', 'P34312', 'P34671', 'P34672', 'P34673', 'P34674', 'P34691', 'P34692', 'P34693', 'P34694', 'R34351', 'R34352', 'R34362', 'R34372', 'R3438', 'R34401', 'R34402', 'R34403', 'R34412', 'R34413', 'R34423', 'R3442C', 'R34801', 'R34802', 'R34811', 'R34812', 'T34301', 'T34302', 'T34303', 'T34304', 'T34305', 'T34306', 'U34751', 'U34752', 'U34761', 'U34762', 'V34021', 'V34022', 'V34023', 'W34051', 'W34052', 'W34601', 'Z34431', 'Z34433', 'Z34434']

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
        locations_list = ['zoom' if x == '' else x for x in locations_list]

        # Название дисциплин и имена преподавателей
        lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
        lessons_list = [lesson.text.split('                                                                ') for lesson in lessons_list]
        lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]
        lessons_list = [string.replace('\n', '') for string in lessons_list]
        lessons_list = [string.replace('     ', ' ') for string in lessons_list]
        lessons_list = [string.replace(': zoom', '') for string in lessons_list]
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
    if group in allg:
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
    else:
        print('NO GROUP')
        return None


#get_groupschedule('K34202ewerr')
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