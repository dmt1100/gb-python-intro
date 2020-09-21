# задача №1
def div(s1, s2):
    try:
        s1, s2 = int(s1), int(s2)
        div_num = s1 / s2
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    return round(div_num, 2)

n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
print(f"Результат: {div(n1, n2)}")
