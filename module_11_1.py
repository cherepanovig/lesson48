#  Выберу следующие три библиотеки: pillow, pandas, matplotlib

#  Pillow — это библиотека для работы с изображениями. Она позволяет открывать, изменять, сохранять и
#  обрабатывать изображения различными способами. Pillow поддерживает множество форматов изображений и
#  предоставляет удобный интерфейс для работы с ними.

from PIL import Image, ImageFilter, ImageOps, ImageEnhance

# Открываем изображение
image = Image.open('music.jpg')
print("Оригинальное изображение:")
image.show()

# Изменение размера изображения
resized_image = image.resize((800, 600))
print("Измененное изображение (800x600):")
resized_image.show()

# Применение фильтра размытия с радиусом размытия 7
blurred_image = image.filter(ImageFilter.BoxBlur(7))
print("Изображение с примененным фильтром размытия:")
blurred_image.show()

# Инвертирование цветов изображения
inverted_image = ImageOps.invert(image)
print("Инвертированное изображение:")
inverted_image.show()

# Увеличение яркости изображения
bright_image = ImageEnhance.Brightness(image)
bright_image = bright_image.enhance(2.5)
print("Увеличение яркости изображения:")
bright_image.show()


# Перевернутое изображения
mirror_image = ImageOps.mirror(image)
print("Перевернутое изображение:")
mirror_image.show()

# Сохранение перевернутого изображения в другом формате
mirror_image.save('mirror_image.png')

# Pandas — это одна из самых популярных библиотек в Python для работы с данными. Она предоставляет мощные и гибкие
# инструменты для анализа и манипуляции данными. Pandas широко используется в науке о данных, машинном обучении,
# экономике, финансах и других областях. Pandas основан на двух ключевых структурах данных: Series и DataFrame.
# Pandas поддерживает работу с различными форматами данных, такими как CSV, Excel, SQL, JSON и многие другие.

import pandas as pd

# Создание Series из списка
data = pd.Series([10, 20, 30, 40])

# Создание Series с указанием индексов
data_with_index = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print('Создание Series из списка')
print(data)
print('Создание Series с указанием индексов')
print(data_with_index)

# Создание DataFrame из словаря списков
data = {
    'Model': ['Жигули', 'Москвич', 'Волга', 'Запорожец'],
    'Age': [5, 3, 15, 8],
    'City': ['Тольятти', 'Москва', 'Нижнии Новгород', 'Запорожье']
}

df = pd.DataFrame(data)
print('Создание DataFrame из словаря списков')
print(df)

# Запись данных в CSV файл
df.to_csv('data_new.csv', index=False)
print()

# Считываем данные из CSV-файла
f_csv = pd.read_csv('data_new.csv')
# Устанавливаем максимальное количество отображаемых столбцов
pd.set_option('display.max_columns', 3)
print('Просмотр первых четырех строк')
print(f_csv.head(4))
print("Статистика по числовым данным:")
print(f_csv.describe())

# Фильтруем данные: выбираем строки, где значение в колонке 'age' больше 5
filtered_file = f_csv[f_csv['Age'] > 5]
print("\nСтроки, где 'Age' больше 5:")
print(filtered_file)

# Вычисление суммы по колонке 'Age'
age_sum = f_csv['Age'].sum()
print(f"Сумма по колонке 'Age': {age_sum}")

# Вычисление среднего значения по колонке 'Age'
age_car = f_csv['Age'].mean()
print(f"Среднее значение по колонке 'Age': {age_car}")

# Matplotlib — библиотека для создания визуализаций, таких как графики, диаграммы и гистограммы.
# Она предоставляет гибкие и мощные инструменты для визуализации данных.

import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Создание графика
plt.plot(x, y, label='Линейная зависимость', color='blue', marker='*')

# Настройка графика
plt.title('Пример линейного графика')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.legend()  # Добавление легенды
plt.grid(True)  # Добавление сетки

# Показ графика
plt.show()

# Данные для визуализации для второго варианта
categories = ['Category A', 'Category B', 'Category C']
values = [23, 45, 56]

# Создаем столбчатую диаграмму
plt.bar(categories, values)
plt.title('Столбчатая диаграмма')
plt.xlabel('Категории')
plt.ylabel('Значения')

# Показываем диаграмму
plt.show()

# Создаем круговую диаграмму
plt.pie(values, labels=categories, autopct='%1.1f%%') # autopct='%1.1f%%' — это формат отображения процентов внутри
# каждого сектора. В данном случае проценты будут отображены с одной цифрой после запятой
plt.title('Круговая диаграмма')

# Показываем диаграмму
plt.show()





