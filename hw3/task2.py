# задача №2
def user_data(**kwargs):
    return ' , '.join(kwargs.values())

print(user_data(name = input("Введите имя: "), surname = input("Введите фамилию: "), birthday = input("Введите день рождения: "), city = input("Введите город проживания: "), email = input("Введите email: "), phone = input("Введите телефон: ")))