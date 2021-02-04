import sys


class VectorError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "Vector Error\n" + self.text


class Vector:
    """
    This class is a vector that can perform mathematical operations.

    Parameters
    ----------
    arg : list of float or int or tuple
        - a list of floats: Vector([0.0, 1.0, 2.0, 3.0])
        - int: Vector(3): [0.0, 1.0, 2.0]
        - tuple (min, max): Vector((10,14)): [10.0, 11.0, 12.0, 13.0]

    """

    def __init__(self, arg):
        try:
            if type(arg) is list:
                if len(arg) == 0:
                    raise VectorError('list must not be empty.')
                self.values = [float(e) for e in arg]
                self.size = len(arg)
            elif type(arg) is int:
                if arg < 1:
                    raise VectorError('Negative and zero values '
                                      + 'are not accepted.')
                self.values = [float(e) for e in range(arg)]
                self.size = arg
            elif type(arg) is tuple:
                if len(arg) != 2:
                    raise VectorError('tuple size is only 2')
                if type(arg[0]) is not int or type(arg[1]) is not int:
                    raise VectorError('Tuple elements are int only')
                if arg[0] >= arg[1]:
                    raise VectorError('Make the value of the second '
                                      + 'argument larger than the first one')
                self.values = [float(e) for e in range(arg[0], arg[1])]
                self.size = arg[1] - arg[0]
            else:
                raise VectorError('arg is list or int or tuple')
        except VectorError as e:
            print(e)
            sys.exit()
        except Exception as e:
            print('arg : list of float or int or tuple')
            print('    - list of floats: Vector([0.0, 1.0, 2.0, 3.0])')
            print('    - int: Vector(3): [0.0, 1.0, 2.0]')
            print('    - tuple (min, max): Vector((10,12)): [10.0, 11.0])')
            print(e)
            sys.exit()

    def __str__(self):
        return '(Vector {})'.format(self.values)

    def __repr__(self):
        return '(Vector {})'.format(self.values)

    def _add_vec(self, vec):
        try:
            if self.size != vec.size:
                raise VectorError('Mismatch in vector size.')
            vec = [self.values[i] + vec.values[i]
                   for i in range(self.size)]
            return Vector(vec)
        except VectorError as e:
            print(e)
            sys.exit()

    def _add_scalar(self, scalar):
        try:
            num = float(scalar)
            vec = [value + num for value in self.values]
            return Vector(vec)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def _multi_vec(self, vec):
        try:
            if self.size != vec.size:
                raise VectorError('Mismatch in vector size.')
            vec = [self.values[i] * vec.values[i]
                   for i in range(self.size)]
            return Vector(vec)
        except VectorError as e:
            print(e)
            sys.exit()

    def _multi_scalar(self, scalar):
        try:
            num = float(scalar)
            vec = [value * num for value in self.values]
            return Vector(vec)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def _div_scalar(self, scalar):
        try:
            num = float(scalar)
            vec = [value / num for value in self.values]
            return Vector(vec)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def _rdiv_scalar(self, scalar):
        try:
            num = float(scalar)
            vec = [num / value for value in self.values]
            return Vector(vec)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def __add__(self, right):
        if type(right) is Vector:
            return self._add_vec(right)
        return self._add_scalar(right)

    def __radd__(self, left):
        return self._add_scalar(left)

    def __sub__(self, right):
        try:
            if type(right) is Vector:
                return self._add_vec(right._multi_scalar(-1))
            return self._add_scalar(-1 * right)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def __rsub__(self, left):
        return self._multi_scalar(-1)._add_scalar(left)

    def __mul__(self, right):
        if type(right) is Vector:
            return self._multi_vec(right)
        return self._multi_scalar(right)

    def __rmul__(self, left):
        return self._multi_scalar(left)

    def __truediv__(self, right):
        return self._div_scalar(right)

    def __rtruediv__(self, left):
        return self._rdiv_scalar(left)
