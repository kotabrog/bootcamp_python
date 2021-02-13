import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst, dtype=None):
        if dtype:
            return np.array(lst, dtype)
        return np.array(lst)

    def from_tuple(self, tpl, dtype=None):
        return self.from_list(tpl, dtype)

    def from_iterable(self, itr, dtype=None):
        return self.from_list(itr, dtype)

    def from_shape(self, shape, value=0, dtype=None):
        if dtype:
            return np.full(shape, value, dtype)
        return np.full(shape, value)

    def random(self, shape, dtype=None):
        if dtype:
            return np.random.rand(*shape).astype(dtype)
        return np.random.rand(*shape)

    def identity(self, n, dtype=None):
        if dtype:
            return np.identity(n, dtype)
        return np.identity(n)


if __name__ == "__main__":
    npc = NumPyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(type(npc.from_list([[1, 2, 3], [6, 3, 4]])))
    print(npc.from_list([[1, 2, 3], [6, 3, 4]], float))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_tuple(([1, 2, 3], [6, 3, 4])))
    print(npc.from_tuple(((1, 2, 3), (6, 3, 4))))
    print(npc.from_tuple(((1, 2, 3), (6, 3, 4)), float))
    print(npc.from_iterable(range(5)))
    print(npc.from_iterable(range(5), float))
    print(type(npc.from_iterable(range(5))))
    shape = (3, 5)
    print(npc.from_shape(shape))
    print(npc.from_shape(shape, 3.1))
    print(npc.from_shape(shape, 3.1, int))
    print(npc.random(shape))
    print(npc.random(shape, int))
    print(npc.identity(4))
    print(npc.identity(4, int))
