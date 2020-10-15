# задача №3
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сложение ячеек: {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше или равно второй, вычитание невозможно!"

    def __mul__(self, other):
        return f'Умножение ячеек: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Деление ячеек: {self.nums // other.nums}'


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
