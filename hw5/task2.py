# задача №2
with open('file2.txt', encoding='utf-8') as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        number_words = len(value.split())
        print(f'Строка {index} содержит {number_words} слов')
