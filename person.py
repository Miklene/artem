from home import Home
from random import randint


class Person:
    def __init__(self, name, home):
        self._name = name
        self._satiety = 50
        self._home = home

    def eat(self):
        food = self._home.get_food_from_fridge(10)
        print(f"{self._name} съел {food} еды")
        self._satiety += food
        print(f"{self._name} сытость: {self._satiety}")

    def work(self):
        print(f"{self._name} поработал")
        self._satiety -= 10
        self._home.put_money_in_nightstand(2)

    def play(self):
        print(f"{self._name} поиграл")
        self._satiety -= 10

    def go_to_market(self):
        print(f"{self._name} сходил в магазин")
        money = self._home.get_money_from_nightstand(10)
        self._home.put_food_in_fridge(money)

    def die(self):
        print(f"{self._name} умер!")

    def live_one_day(self):
        if self._satiety <= 0:
            self.die()
        cube = randint(1, 6)
        if self._satiety < 20:
            self.eat()
        elif self._home.food < 10:
            self.go_to_market()
        elif self._home.money < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

