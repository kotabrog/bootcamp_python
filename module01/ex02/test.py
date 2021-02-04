import sys
from vector import Vector

vec = Vector([0, 1, 2])
# vec = Vector(4)
# vec = Vector((2, 7))
# vec = Vector(['a'])
# vec = Vector('a')
# vec = Vector(0)
# vec = Vector(-1)
# vec = Vector((0, 0))
# vec = Vector((0))
# vec = Vector((5, 2, 6))
# vec = Vector([])
# vec = Vector(())

vec2 = Vector([0, 2, 4])
vec4 = Vector([0, 2])
vec3 = vec + vec2
# vec3 = vec + 1
# vec3 = vec + vec4
# vec3 = vec + 'd'
# vec3 = 1 + vec
# vec3 = 'd' + vec
# vec3 = vec - vec2
# vec3 = vec - 1
# vec3 = vec - vec4
# vec3 = vec - 'd'
# vec3 = 1 - vec
# vec3 = 'd' - vec
# vec3 = vec - {'a': 1}
# vec3 = vec * vec2
# vec3 = vec * 2
# vec3 = vec * vec4
# vec3 = vec * 'a'
# vec3 = 2 * vec
# vec3 = {'a': 1} * vec
# vec3 = vec / vec2
# vec3 = vec / 2
# vec3 = vec / 'a'
# vec3 = 2 / vec
vec5 = Vector([1, 2, 4])
# vec3 = 2 / vec5
# vec3 = 'a' / vec5

print(vec3.values)
print(vec3.size)
print(vec3)
