# задача №5
class Stationery:
    def __init__(self, title="Канцелярская принадлежность."):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с ручкой {self.title}!")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с карандашом {self.title}!")


class Marker(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с маркером {self.title}!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("COPIC")
marker.draw()
