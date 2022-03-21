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

 #   def __str__(self):  # Добавленный метод
 #       return f'{self.name} имеет оклад {self.pay} должность: {(self.job if self.job != None else "не назначен!")}'


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mng', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaise(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == "__main__":
    bob = Person('Bob Smith')  # Тестирование класса
    sue = Person('Sue Jones', 'dev', 100000)  # Автоматически выполняет__init__
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaise(.1)
    development.showAll()