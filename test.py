from operator import attrgetter

class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def x(self):
        return self.x
    def y(self):
        return self.y
    def __str__(self):
        return 'A({},{})'.format(self.x, self.y)

l = [A(3,4), A(1,3), A(2,1), A(5,2), A(4,5)]
print max(l, key=attrgetter('x'))
print min(l, key=attrgetter('x'))
print max(l, key=attrgetter('y'))
print min(l, key=attrgetter('y'))

print ",".join(str(a) for a in sorted(l, key=attrgetter('x')))
print ",".join(str(a) for a in sorted(l, key=attrgetter('y')))

print ",".join(str(a) for a in sorted(l, key=attrgetter('x'), reverse = True))
print ",".join(str(a) for a in sorted(l, key=attrgetter('y'), reverse = True))