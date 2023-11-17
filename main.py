from home import Home
from person import Person


home = Home()
artem = Person("Artem", home)
girlfriend = Person("Tamara", home)
for day in range(365):
    print(f"День {day}")
    artem.live_one_day()
    girlfriend.live_one_day()
