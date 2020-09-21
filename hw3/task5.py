# задача №5
def my_func():
    sum = 0
    while True:
        my_list = input("Введите число, для выхода введите - 'q': ").split()
        for num in my_list:
            if num == 'q':
                return sum
            else:
                try:
                    sum += int(num)
                except ValueError:
                    print("Для выхода введите - 'q': ")
        print(f"Сумма чисел равна = {sum}")
print(f"Сумма чисел равна = {my_func()}")