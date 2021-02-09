import sys


def ft_map(function_to_apply, list_of_inputs):
    try:
        for input in list_of_inputs:
            yield function_to_apply(input)
    except Exception as e:
        print("{}:".format(e.__class__.__name__), e)
        sys.exit()


class Hoge:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'value: {}'.format(self.value)


if __name__ == '__main__':
    sample = [1.1, 2.1, 3.1, 4.1]
    # sample = (1.1, 2.1, 3.1, 4.1)
    # sample = {1.1: 2, 2.1: 3, 3.1: 4, 4.1: 5}
    # sample = {1.1: 2, 2.1: 3, 3.1: 4, 4.1: 5}
    # sample = range(5)
    # sample = 3
    # sample = None
    func = int
    # func = lambda x: x + 1
    # func = Hoge
    # func = list
    map_object = map(func, sample)
    ft_map_object = ft_map(func, sample)
    print(type(map_object))
    print(type(ft_map_object))

    # help(map)

    print(map_object)
    print(ft_map_object)

    print(next(map_object))
    print(next(ft_map_object))

    for temp in map_object:
        print(temp)

    for temp in ft_map_object:
        print(temp)
