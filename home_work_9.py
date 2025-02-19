from marvel import full_dict
import pprint

def user_value(value):
#  функция для превращения, вводимой пользователем строки в список
# принимает - стороку с цифрами, возвращает - список с цифрами
    try:
        return int(value)
    except ValueError:
        return None
user_input = input("Вводите числа через пробел")
numbers = list(map(user_value, user_input.split()))


valid_ids = list(filter(lambda x: x is not None, numbers))
# Удаление None из списка valid_ids

filtered_movies_dict = {movie_id: full_dict[movie_id] for movie_id in valid_ids if movie_id in full_dict}

# Фильтрация списка фильмов на основе valid_ids c использованием генератора словарей

directors = {movie['director'] for movie in filtered_movies_dict.values()}
# Создание множества уникальных значений ключа 'director' с помощью set comprehension

full_dict_copy = {
    movie_id: {k: (str(v) if k == 'year' else v) for k, v in movie.items()}
    for movie_id, movie in full_dict.items()
}
# Создание копии словаря с преобразованием значений 'year' в строку с помощью dict comprehension



filtered_movies = filter(lambda movie: movie['title'].startswith('Ч'), full_dict.values())
# Использование filter для получения фильмов, названия которых начинаются на букву 'Ч'


sorted_full_dict = {
    movie_id: movie for movie_id, movie in sorted(full_dict.items(), key=lambda item: item[1]['director'])
}
# Сортировка словаря по значению ключа 'director' в алфавитном порядке
pprint.pprint(sorted_full_dict)
print("\nЗадание отсортировать словарь по одному параметру по именам режисеров в алфавитном порядке")




sorted_full_dict = {
    movie_id: movie for movie_id, movie in sorted(
        full_dict.items(),
        key=lambda item: (
            item[1]['director'] if item[1]['director'] is not None else '',
            item[1]['title'] if item[1]['title'] is not None else ''
        )
    )
}
# Сортировка словаря по значению ключа 'director' в алфавитном порядке и по значению 'title' в алфавитном порядке
pprint.pprint(sorted_full_dict)
print("\nЗадание отсортировать словарь по двум параметрам (по именам режисеров в алфавитном порядки и по названию в алфавитном порядке)")


sorted_filtered_full_dict = {
    movie_id: movie for movie_id, movie in sorted(
        filter(lambda item: item[1]['director'] is not None and item[1]['title'] is not None, full_dict.items()),
        key=lambda item: (item[1]['director'], item[1]['title'])
    )
}
# Фильтрация и сортировка словаря с использованием filter и sorted

pprint.pprint(sorted_filtered_full_dict)

# Красивый вывод результатов с использованием pprint

print("\nЗадание: Отфильтровать и отсортировать словарь `full_dict` по значению `director` в алфавитном порядке и по значению `title` в алфавитном порядке.")
# Подпись о выполненном задании