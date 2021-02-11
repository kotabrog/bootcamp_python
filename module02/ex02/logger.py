import time
from random import randint
import getpass


def log(func):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time
        ms_flag = False
        if elapsed_time < 1:
            elapsed_time *= 1000
            ms_flag = True
        func_name = func.__name__.split('_')
        func_name = ' '.join(map(lambda x: x.capitalize(), func_name))
        with open('machine.log', 'a') as f:
            print('({})Running: {} 	[ exec-time = {:.3f} {} ]'.format(
                  getpass.getuser(),
                  func_name,
                  elapsed_time,
                  'ms' if ms_flag else 's'), file=f)
        return ret
    return inner


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
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
