from matrix import Matrix

# a = Matrix([[1, 2, 3], [3, 4, 5]])
# a = Matrix((3, 2))
# a = Matrix([[1, 2, 3], [3, 4, 5]], (2, 3))
# a = Matrix((1, 1))
# a = Matrix([])
# a = Matrix([[]])
# a = Matrix([[[]]])
# a = Matrix([[1, 2, 3], [3, 4, 5]], (3, 3))
# a = Matrix([[1, 2, 3], [3, 4]])
# a = Matrix((2.0, 3.0))
# a = Matrix((2, 3, 4))

b = Matrix([[1, 2, 3], [3, 4, 5]])
c = Matrix([[2, 4, 6], [6, 8, 10]])
c = Matrix([[2, 0, 6], [6, 8, 10]])
# c = Matrix([[1, 2], [3, 4], [5, 6]])
# c = Matrix([[2, 4], [6, 8]])
# b = Matrix([[2, 4], [6, 8]])
# c = Matrix([[3]])
# c = Matrix([[0]])
# b = Matrix([[3]])
# b = Matrix([[0]])
# c = 3
# b = 3
# a = b + c
# a = b - c
# a = b * c
a = b / c


print(a)
print(a.shape)
