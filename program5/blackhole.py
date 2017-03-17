# A Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    
    radius = 10
        
    def __init__(self,x,y):
        Simulton.__init__(self,x,y, 2*Black_Hole.radius, 2*Black_Hole.radius)
    
    def update(self, model):
            check_set = set()
            def locations(i):
                return self.contains(i.get_location())
            eat = model.find(lambda x: isinstance(x, Prey) and locations(x))
            for i in eat:
                if self.contains(i.get_location()):
                    check_set.add(i)
                    model.remove(i)
            return check_set
    
    def display(self, the_canvas):
            width,height = self.get_dimension()
            the_canvas.create_oval(self._x-width/2, self._y-height/2, self._x+width/2, self._y+height/2,fill = "black")

    def contains(self, xy):
        return self.distance(xy) <= self.get_dimension()[0]/2