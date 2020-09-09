# задача №2
time_sec = int(input("Введите время в секундах: "))
hours = time_sec // 3600
delta_hours = time_sec % 3600
minutes = delta_hours // 60
seconds = delta_hours % 60
print("Время в формате (чч:мм:сс): "
      + '{:02}'.format(hours) + ':'
      + '{:02}'.format(minutes) + ':'
      + '{:02}'.format(seconds))
