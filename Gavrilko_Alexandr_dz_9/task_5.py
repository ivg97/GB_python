# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен
# выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

def draw_all(func):
    def wraps(*args):
        print('Запуск отрисовки')
        result = func(*args)
        return result
    return wraps


class Stationery():

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    @draw_all
    def draw(self):
        print(f'{self.title} пишет!')



class Pencil(Stationery):
    @draw_all
    def draw(self):
        print(f'{self.title} рисует!')


class Handle(Stationery):
    @draw_all
    def draw(self):
        print(f'{self.title} чертит!')

pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()