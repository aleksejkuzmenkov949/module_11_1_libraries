import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # выводим статус-код ответа

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json())  # выводим данные, отправленные на сервер

response = requests.get('https://api.github.com')
print(response.headers)  # выводим заголовки ответа


# Библиотека requests
# - Возможности:
#   - Выполнение HTTP-запросов (GET, POST и т.д.).
#   - Обработка форм и куки.
#   - Поддержка API.

import pandas as pd

# Импорт библиотеки и создание DataFrame

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Сортировка данных

sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)

# Добавление нового столбца

df['Salary'] = [70000, 80000, 90000]
print(df)

# Библиотека pandas
# - Возможности:
#   - Чтение и запись данных в различных форматах (CSV, Excel и т.д.).
#   - Обработка и анализ данных с помощью DataFrame и Series.
#   - Проведение операции группировки и агрегации


import numpy as np

# Создание массива и базовые операции

array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Математические операции с массивом

sum_array = np.sum(array)  # вычисляем сумму элементов массива
mean_array = np.mean(array)  # вычисляем среднее значение
print(f'Sum: {sum_array}, Mean: {mean_array}')


# Генерация случайных чисел

random_array = np.random.rand(5)  # создаем массив из 5 случайных чисел
print("Random Array:", random_array)

# Библиотека numpy
# - Возможности:
#   - Создание и управление многомерными массивами.
#   - Выполнение математических операций и линейной алгебры.
#   - Генерация случайных чисел и работа с статистикой.