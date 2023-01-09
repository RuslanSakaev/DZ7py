def contact_to_s():
    return input('Введите информацию для поиска:  ')


def choose_model():
    return input('Что делаем? (1 - добавляем, 2 - ищем) ')


def new_contact():
    name = input('Введите имя: ')
    phone_num = input('Введите номер: ')
    return f'{name} || {phone_num}'


def show_found(result):
    print('Результат поиска: ')
    for i in result:
        print(i)
