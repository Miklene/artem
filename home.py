class Home:
    def __init__(self):
        self._fridge = 50
        self._nightstand_with_money = 0

    def get_food_from_fridge(self, amount):
        if self._fridge < amount:
            amount = min(self._fridge, amount)
        self._fridge -= amount
        print(f"В холодильнике {self._fridge} еды")
        return amount

    def get_money_from_nightstand(self, amount):
        if self._nightstand_with_money < amount:
            amount = min(self._nightstand_with_money, amount)
        self._nightstand_with_money -= amount
        print(f"В тумбочке {self._nightstand_with_money} денег")
        return amount

    def put_food_in_fridge(self, food):
        self._fridge += food
        print(f"В холодильнике {self._fridge} еды")

    def put_money_in_nightstand(self, money):
        self._nightstand_with_money += money
        print(f"В тумбочке {self._nightstand_with_money} денег")

    @property
    def food(self):
        return self._fridge

    @property
    def money(self):
        return self._nightstand_with_money
