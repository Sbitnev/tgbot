# import datetime

# def get_day_and_week():
#     today = datetime.date.today()
#     day_of_week = today.weekday()  # Monday - 0, Sunday - 6
#     even_week = 1 if (today.isocalendar()[1] % 2 == 0) else 0  # 0 for odd week, 1 for even
#     return even_week, day_of_week

# print(get_day_and_week())

# locations_list = ['zoom', '', 'location', '', 'zoom', 'mapview']
# locations_list = ['zoom' if x == '' else x for x in locations_list]
# print(locations_list)

a = {
"Monday": [
    {
        "time": "10:00-11:30",
        "addr": "zoom",
        "info": "Виртуализация сетевых функций(Лек), Аминов Натиг Сабит оглы, Дистанционный"
    },
    {
        "time": "11:40-13:10",
        "addr": "zoom",
        "info": "Виртуализация сетевых функций(Прак), Аминов Натиг Сабит оглы, Дистанционный"
    },
    {
        "time": "13:30-15:00",
        "addr": "zoom",
        "info": "Виртуализация сетевых функций(Лаб), Аминов Натиг Сабит оглы, Дистанционный"
    }]
            }

def format_schedule(schedule_dict):
    output = ""
    for day, classes in schedule_dict.items():
        output += f"Расписание на {day}:\n"
        for class_info in classes:
            arr = class_info['info'].split(", ")
            output += f"Время: {class_info['time']}\n"
            output += f"Место: {class_info['addr']}\n"
            output += f"Предмет: {arr[0]}\n"
            output += f"Преподаватель: {arr[1]}\n"
            output += f"Формат: {arr[2]}\n\n"
    return output

print(format_schedule(a))