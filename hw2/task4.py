# задача №4
string = input("Введите строку из нескольких слов, разделенных пробелами: ").split()
for i, y in enumerate(string, 1):
    print(i, y[:10])
