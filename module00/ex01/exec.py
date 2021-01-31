from sys import argv

print(*list(map(lambda x: x[::-1].swapcase(), argv[1:]))[::-1])
