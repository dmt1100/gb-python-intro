# задача №4
def my_func(x, y):
    try:
        x, y = float(x), int(y)
        result = x ** y
    except ValueError:
        return "Вводить нужно числа!"
    return round(result, 4)
n1 = input("Введите действительное положительное число x: ")
n2 = input("Введите целое отрицательное число y: ")
print(my_func(n1, n2))