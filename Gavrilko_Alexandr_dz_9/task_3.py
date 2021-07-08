# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать
# данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():

    def __init__(self, name, surname, position, _incone):
        self.name = name
        self.surname = surname
        self.position = position
        self._incone = _incone




class Position(Worker):

    def __init__(self, name, surname, position, _incone):
        super().__init__(name, surname, position, _incone)

    def get_full_name(self):
        print(f'{self.name} {self.surname} - {self.position}')

    def get_total_income(self):
        print(f'{self.surname} - {self._incone["wage"] + self._incone["bonus"]}')


position = Position('Ivan', 'Ivanov', 'Developer', {'wage': 50000, 'bonus': 15000})
position.get_full_name()
position.get_total_income()


