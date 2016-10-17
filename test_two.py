''' self is test duece module '''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._test = 'abc'
    
    def area(self):
        return math.pi * self.radius ** 2.0

    def perimiter(self):
        return math.pi * self.radius * 2.0


class Tire( Circle ):
    def perimiter(self):
        return Circle.perimiter(self) * 1.5 # extending methon (not overwriting)


# test
c = Circle(5)
print( 'Area: {:0.3f}'.format(c.area()) )
print( 'Perimiter: {:0.3f}'.format(c.perimiter()) )

t = Tire(5)
print( 'Tire Perimiter: {:0.3f}'.format(t.perimiter()) )

print( 'test: {} '.format( c._test ) )

