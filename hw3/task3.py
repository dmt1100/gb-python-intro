#задача №3
def my_func(n1, n2, n3):
    my_list = [n1, n2, n3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return "Вводить нужно только числа!"
print(my_func(15, -7, 20))