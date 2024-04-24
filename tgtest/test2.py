# import datetime

# def get_day_and_week():
#     days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     today = datetime.date.today()
#     day_of_week = today.weekday()  # Monday - 0, Sunday - 6
#     even_week = "odd" if (today.isocalendar()[1] % 2 == 0) else "even"  # 0 for odd week, 1 for even
#     return even_week, day_of_week

# result = get_day_and_week()
# week, day = get_day_and_week()

# print(week)
# print(day)