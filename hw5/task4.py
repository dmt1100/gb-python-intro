#задача №4
"""
rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file44.txt", "w", encoding='utf-8') as new_file:
    with open("file4.txt", encoding='utf-8') as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dic[i[0]] + ' - ' + i[1] + "\n")
"""
from googletrans import Translator
with open("file4_translate.txt", "w", encoding='utf-8') as f:
    with open("file4.txt", encoding='utf-8') as f1:
        text = f1.read()
    f.write(Translator().translate(text, dest='ru').text)
