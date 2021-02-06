import sys


class MatrixError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "Matrix Error\n" + self.text


class Matrix:
    """
    This class is a matrix that can perform mathematical operations.

    Parameters
    ----------
    arg : list of float or int or tuple
        - a list of lists: Matrix([[0.0, 1.0, 2.0], [4.0, 5.0, 6.0]])
        - a shape (rows, columns): Matrix((3, 3))
        -> by default the matrix will be filled with zeroes
        - the expected elements and shape:
        -> Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))

    """

    def __init__(self, arg1, arg2=None):
        try:
            if type(arg1) is list:
                if len(arg1) == 0 or len(arg1[0]) == 0:
                    raise MatrixError('list must not be empty.')
                self.shape = (len(arg1), len(arg1[0]))
                if arg2 and arg2 != self.shape:
                    raise MatrixError('If you specify list and shape, '
                                      + 'make sure to match the shap.')
                self.data = []
                for row in arg1:
                    if len(row) != len(arg1[0]):
                        raise MatrixError('The size of all lists '
                                          + 'within a list is the same.')
                    self.data.append([float(e) for e in row])
            elif type(arg1) is tuple:
                if len(arg1) != 2:
                    raise MatrixError('tuple size is only 2')
                if type(arg1[0]) is not int or type(arg1[1]) is not int:
                    raise MatrixError('Tuple elements are int only')
                if arg1[0] < 1 or arg1[1] < 1:
                    raise MatrixError('shape should be a value '
                                      + 'greater than or equal to 1')
                self.data = [[float(0)] * arg1[1] for i in range(arg1[0])]
                self.shape = (arg1[0], arg1[1])
            else:
                raise MatrixError('arg is list or int or tuple')
        except MatrixError as e:
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
        return '(Matrix {})'.format(self.data)

    def __repr__(self):
        return '(Matrix {})'.format(self.data)

    def _size_check(self, matrix, mode='+'):
        try:
            if mode == '+':
                if self.shape != matrix.shape:
                    raise MatrixError('For this operator, '
                                      + 'match the matrix shape')
            elif mode == '*':
                if self.shape[1] != matrix.shape[0]:
                    raise MatrixError('For this operator, '
                                      + 'the shape is not correct')
            else:
                raise MatrixError('The mode is wrong.')
        except MatrixError as e:
            print(e)
            sys.exit()

    def _add_matrix(self, matrix):
        try:
            if type(matrix) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            self._size_check(matrix)
            data = [[self.data[i][j] + matrix.data[i][j]
                    for j in range(self.shape[1])]
                    for i in range(self.shape[0])]
            return Matrix(data)
        except MatrixError as e:
            print(e)
            sys.exit()

    def _multi_scalar(self, scaler):
        try:
            num = float(scaler)
            data = [[self.data[i][j] * num
                    for j in range(self.shape[1])]
                    for i in range(self.shape[0])]
            return Matrix(data)
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def _rdiv_scalar(self, scaler):
        try:
            num = float(scaler)
            data = [[num / self.data[i][j]
                    for j in range(self.shape[1])]
                    for i in range(self.shape[0])]
            return Matrix(data)
        except ZeroDivisionError as e:
            print('Zero percentages have been generated.')
            print(e)
            sys.exit()
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def _multi_matrix(self, matrix):
        try:
            if type(matrix) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            if self.shape == (1, 1):
                return matrix._multi_scalar(self.data[0][0])
            if matrix.shape == (1, 1):
                return self._multi_scalar(matrix.data[0][0])
            self._size_check(matrix, '*')
            data = [[sum([self.data[i][j] * matrix.data[j][k]
                    for j in range(self.shape[1])])
                    for k in range(matrix.shape[1])]
                    for i in range(self.shape[0])]
            return Matrix(data)
        except MatrixError as e:
            print(e)
            sys.exit()

    def __add__(self, right):
        return self._add_matrix(right)

    def __radd__(self, left):
        return self._add_matrix(left)

    def __sub__(self, right):
        try:
            if type(right) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            return self._add_matrix(right._multi_scalar(-1))
        except MatrixError as e:
            print(e)
            sys.exit()

    def __rsub__(self, left):
        return self._multi_scalar(-1)._add_matrix(left)

    def __mul__(self, right):
        return self._multi_matrix(right)

    def __rmul__(self, left):
        try:
            if type(left) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            return left._multi_matrix(self)
        except MatrixError as e:
            print(e)
            sys.exit()

    def __truediv__(self, right):
        try:
            if type(right) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            if self.shape == (1, 1):
                return right._rdiv_scalar(self.data[0][0])
            if right.shape == (1, 1):
                return self._multi_scalar(1 / right.data[0][0])
            raise MatrixError('One of the shapes must be (1, 1)')
        except MatrixError as e:
            print(e)
            sys.exit()
        except ZeroDivisionError as e:
            print('Zero percentages have been generated.')
            print(e)
            sys.exit()
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()

    def __rtruediv__(self, left):
        try:
            if type(left) is not Matrix:
                raise MatrixError('Operand that does not '
                                  + 'support this operator.')
            if left.shape == (1, 1):
                return self._rdiv_scalar(left.data[0][0])
            if self.shape == (1, 1):
                return left._multi_scalar(1 / self.data[0][0])
            raise MatrixError('One of the shapes must be (1, 1)')
        except MatrixError as e:
            print(e)
            sys.exit()
        except ZeroDivisionError as e:
            print('Zero percentages have been generated.')
            print(e)
            sys.exit()
        except Exception as e:
            print('Operand that does not support this operator.')
            print(e)
            sys.exit()
