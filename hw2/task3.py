# задача №3
month = int(input("Введите месяц от 1 до 12: "))
season = [{'январь': 'зима'},
          {'февраль': 'зима'},
          {'март': 'весна'},
          {'апрель': 'весна'},
          {'май': 'весна'},
          {'июнь': 'лето'},
          {'июль': 'лето'},
          {'август': 'лето'},
          {'сентябрь': 'осень'},
          {'октябрь': 'осень'},
          {'ноябрь': 'осень'},
          {'декабрь': 'зима'}]
dict_s = season[month - 1]
for key, value in dict_s.items():
    print(f"Вы выбрали месяц - {key}, который находится в сезоне - {value}")
