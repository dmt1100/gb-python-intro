# задача №1
from sys import argv

try:
    hours, rate, premium = map(float, argv[1:])
    print(f"Заработная плата равна = {hours * rate + premium}")
except ValueError:
    print("Введите 3 числа!")
