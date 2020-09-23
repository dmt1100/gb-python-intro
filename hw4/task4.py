# задача №4
from random import randint

my_list = [randint(1, 10) for i in range(10)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Исходный список: {my_list}\nНовый список: {new_list}")
