# задача №2
time_sec = int(input("Введите время в секундах: "))
hours = str(time_sec // 3600)
delta_hours = time_sec % 3600
minutes = str(delta_hours // 60)
seconds = str(delta_hours % 60)
if len(hours) < 2:
    hours = '0' + hours
if len(minutes) < 2:
    minutes = '0' + minutes
if len(seconds) < 2:
    seconds = '0' + seconds
print(f"Время в формате (чч:мм:сс): {hours}:{minutes}:{seconds}")
