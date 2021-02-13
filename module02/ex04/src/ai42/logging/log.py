import time
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
