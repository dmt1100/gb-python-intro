# задача № 3
with open('file3.txt', 'r', encoding='utf-8') as f:
    sums = []
    less = []
    line = f.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        sums.append(i[1])

print(f'Оклад меньше 20000 {less}, средняя величина = {sum(map(float, sums)) / len(sums)}')
