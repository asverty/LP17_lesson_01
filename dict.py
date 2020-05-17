dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
print(dict_1['city'])

# уменьшение значения "temperature" на 5 градусов
dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
dict_1['temperature'] = '15'
print(dict_1)

# проверка, в словаре ключа country
dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
dict_1['temperature'] = '15'
print(dict_1.get('county'))

# выведение значения по-умолчанию "Россия" для ключа country
dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
dict_1['temperature'] = '15'
dict_1.get('country', 'Россия')
print(dict_1)

# Добавление в словарь элемента date со значением "27.05.2019"
dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
dict_1['temperature'] = '15'
dict_1.get('country', 'Россия')
dict_1['date'] = '27.05.2019'
print(dict_1)

# длина словаря
dict_1 = {
    'city': 'Москва', 
    'temperature': '20'
}
dict_1['temperature'] = '15'
dict_1.get('country', 'Россия')
dict_1['date'] = '27.05.2019'
print(len(dict_1))
