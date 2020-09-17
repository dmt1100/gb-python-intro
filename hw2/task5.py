# задача №5
my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {my_list}")
rating = int(input("Введите рейтинг: "))
y = 0
for i in my_list:
    if rating <= i:
        y += 1
my_list.insert(y, rating)
print(my_list)
