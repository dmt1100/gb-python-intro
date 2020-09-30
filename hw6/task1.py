# задача №1
from time import sleep


class TrafficLight:
    __color = "Белый"

    def work(self):
        while True:
            print('Красный свет')
            sleep(7)
            print('Желтый свет')
            sleep(2)
            print('Зеленый свет')
            sleep(10)
            print('Желтый свет')
            sleep(2)


TrafficLight = TrafficLight()
TrafficLight.work()
