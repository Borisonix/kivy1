class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):  # Добавленный метод
        return '[Person: %s, %s]' % (self.name, self.pay)

    def __str__(self):  # Добавленный метод
        return f'{self.name} имеет оклад {self.pay} должность: {(self.job if self.job != None else "не назначен!")}'


class Manager():
    def __init__(self, name, pay):
        self.person = Person(name, 'mng', pay)  # Внедрить объект Person

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)  # Перехватить и делегировать

    def __getattr__(self, attr):
        return getattr(self.person, attr)    # Делегировать все остальные атрибуты

    def __repr__(self):
        return str(self.person)


if __name__ == "__main__":
    bob = Person('Bob Smith')  # Тестирование класса
    sue = Person('Sue Jones', 'dev', 100000)  # Автоматически выполняет__init__
    print(bob)  # Извлечение присоединенных атрибутов
    print(sue)  # Атрибуты sue и bob отличаются
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--All three—')
    for obj in (bob, sue, tom):  # Обработать объекты обобщенным образом
        obj.giveRaise(.10)
        print(obj)
