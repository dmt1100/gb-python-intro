# задача №5
proceed = float(input("Введите выручку: "))
cost = float(input("Введите издержки: "))
if proceed > cost:
    print("Фирма работает с прибылью.")
    print(f"Рентабельность составляет: {proceed / cost:.2f}")
    count = int(input("Введите численность сотрудников: "))
    print(f"Прибыль фирмы на одного сотрудника: {(proceed - cost) / count:.2f}")
elif cost > proceed:
    print("Фирма работает в убыток.")
else:
    print("Выручка и издержки равны.")
