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

print(directors)