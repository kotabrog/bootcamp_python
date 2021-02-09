import sys


def ft_filter(function_to_apply, list_of_inputs):
    try:
        if function_to_apply is None:
            for input in list_of_inputs:
                yield input
        else:
            for input in list_of_inputs:
                if function_to_apply(input):
                    yield input
    except Exception as e:
        print("{}:".format(e.__class__.__name__), e)
        sys.exit()


class HogeHoge:
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    sample = [1.1, 2.1, 3.1, 4.1]
    # sample = (1.1, 2.1, 3.1, 4.1)
    # sample = {1.1: 2, 2.1: 3, 3.1: 4, 4.1: 5}
    # sample = range(5)
    # sample = 3
    # sample = None
    func = lambda x: x > 2
    # func = HogeHoge
    # func = 1
    # func = None
    filter_object = filter(func, sample)
    ft_filter_object = ft_filter(func, sample)
    print(type(filter_object))
    print(type(ft_filter_object))

    print(filter_object)
    print(ft_filter_object)

    print(next(filter_object))
    print(next(ft_filter_object))

    for temp in filter_object:
        print(temp)

    for temp in ft_filter_object:
        print(temp)
