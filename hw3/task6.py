# задача №6
def int_func():
    for word in input("Введите слова через пробел из маленьких латинских букв: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars +=1
        if chars == len(word):
            print(word.title())
        else:
            print(f"Только маленькие латинские буквы!")
int_func()