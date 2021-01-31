t = (19, 42, 21)

s = 'The {} numbers are: '.format(len(t))
for d in t:
    s += str(d) + ', '
s = s[:-2]
print(s)
