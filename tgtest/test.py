import pickle

# Загрузка массива из файла
with open('groups/allgroups.pkl', 'rb') as file:
    loaded_array = pickle.load(file)

# Использование загруженного массива
print(loaded_array)  # Вывод массива в консоль
# Дальнейшее использование массива в коде