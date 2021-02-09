from functools import reduce
from operator import add
import sys


def ft_reduce(function_to_apply, list_of_inputs):
    try:
        for i, input in enumerate(list_of_inputs):
            if i == 0:
                ret = input
            else:
                ret = function_to_apply(ret, input)
        return ret
    except Exception as e:
        print("{}:".format(e.__class__.__name__), e)
        sys.exit()


def sum_print(a, b):
    a = a - b
    print(a)


if __name__ == '__main__':
    sample = [1.1, 2.1, 3.1, 4.1]
    # sample = (1.1, 2.1, 3.1, 4.1)
    # sample = {1.1: 2, 2.1: 3, 3.1: 4, 4.1: 5}
    # sample = range(5)
    # sample = 3
    # sample = None
    func = add
    # func = lambda x, y: x - y
    # func = sum_print
    # func = 1
    # func = None
    reduce_object = reduce(func, sample)
    ft_reduce_object = ft_reduce(func, sample)

    print(type(reduce_object))
    print(type(ft_reduce_object))

    print(reduce_object)
    print(ft_reduce_object)
