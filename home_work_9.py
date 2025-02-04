from marvel import full_dict

def user_value(value):
    try:
        return int(value)
    except ValueError:
        return None
user_input = input("Вводите числа через пробел")
numbers = list(map(user_value, user_input.split()))
print(numbers)
