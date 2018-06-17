__author__ = 'Sergey Khrul'

from training.geom2d.point import Point

a = Point(0, 0)
b = Point(3, 4)
# print(a.distance(b))
# print(a == b)
# print(a == Point(0, 0))

str = 'my test shit'
l1 = [Point(0, 0), Point(3, 2), Point(2, 1)]
# l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
print('l1: ', l1)
print('l2: ',l2)


l = []
for i in range(-5,6):
    l.append(Point(i, i*i))
print('l: ',*l, sep='\n')
l2 = [Point(el.x, -el.y) for el in l]
print('l2: ', l2)


l3 = list(map(lambda i: Point(i, i*i), range(-5, 6)))
print('l3: ', l3)
l4 = list(map(lambda p: Point(p.x, -p.y), l3))
print('l4: ', l4)


l5 = list(filter(lambda p: p.x > 0, l3))
print('l5: ', l5)
l6 = list(filter(lambda p: p.x % 2 == 0, l3))
print('l6: ', l6)
