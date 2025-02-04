from marvel import full_dict

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
print(sorted_full_dict)




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
print(sorted_full_dict)