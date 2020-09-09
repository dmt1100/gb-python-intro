# задача №6
a = float(input("Введите значение a = "))
b = float(input("Введите значение b = "))
p = 0
i = 0
day = 1
print(f"Результат:\n{day}-й день: {a:.2f}")
while a < b:
    p = a * 0.1
    a = a + p
    day += 1
    print(f"{day}-й день: {a:.2f}")
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")
