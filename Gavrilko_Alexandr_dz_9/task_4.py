# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,\
#                                                                                повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Вызовите методы и покажите результат.

class Car():

    def __init__(self, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.is_police = is_police


    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость авто - {self.speed}')



class TownCar(Car):
    limit_max = 60
    def __init__(self, speed, color, is_police):
        super().__init__(speed, color, is_police)

    def show_speed(self):
        if self.speed > self.limit_max:
            print(f'Превышение скорости. Ваша скорость - {self.speed}')
        else:
            print(f'Скорость в норме - {self.speed}')



class SportCar(Car):
    def __init__(self, speed, color, is_police):
        super().__init__(speed, color, is_police)

class WorkCar(Car):
    limit_max = 40
    def __init__(self, speed, color, is_police):
        super().__init__(speed, color, is_police)

    def show_speed(self):
        if self.speed > self.limit_max:
            print(f'Превышение скорости. Ваша скорость - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, is_police):
        super().__init__(speed, color, is_police)
        self.is_police = True

print('------- Town -------')
town = TownCar(65, 'black', False)
town.go()
town.turn('направо')
town.show_speed()
town.stop()
print('\n------- Sport -------')
sport = SportCar(140, 'red', False)
sport.go()
sport.turn('налево')
sport.show_speed()
sport.stop()
print('\n------- Work -------')
work = WorkCar(41, 'blue', False)
work.go()
work.turn('налево')
work.show_speed()
work.stop()
print('\n------- Police -------')
police = PoliceCar(65, 'tricolor', True)
police.go()
police.turn('налево')
police.show_speed()
police.stop()