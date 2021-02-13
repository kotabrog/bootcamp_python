import ai42.progressbar as pg
import ai42.logging.log as lg
from time import sleep, perf_counter
import time
from random import randint
import getpass


class CoffeeMachine():

    water_level = 100

    @lg.log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @lg.log
    def boil_water(self):
        return "boiling..."

    @lg.log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @lg.log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

    listy = range(1000)
    ret = 0
    for elem in pg.ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
