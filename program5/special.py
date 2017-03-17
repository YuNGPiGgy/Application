#This Special Simulton is similar to the combination of blackhole and pulsator
#    where it will "eat" other preys and grow in size
#    however, it will also change color
#    the initial color is white. It will change to red as it eats more preys
#    until it reaches the reddest and biggest, it will explode into 20 small balls

from simulton import Simulton
from prey import Prey
from ball import Ball

class Special(Simulton):

    def __init__(self,x,y, BG = 255, color="white"):
        Simulton.__init__(self,x,y, 10, 10)
        self.decimal_BG = BG
        self.color = color
    
    def update(self, model):
        check_set = set()
        def locations(i):
            return self.contains(i.get_location())
        eat = model.find(lambda x: isinstance(x, Prey) and locations(x))
        for i in eat:
            if self.contains(i.get_location()):
                check_set.add(i)
                model.remove(i)
            self.change_dimension(len(check_set), len(check_set))
            if self.decimal_BG != 21:
                self.decimal_BG -= 9
                self.color = "#ff"+str(hex(self.decimal_BG)[2:])+str(hex(self.decimal_BG)[2:])
            else:
                self.color = "#ff000000"
                
                for _ in range(20):
                    model.simultons.add(eval("Ball" + '(' + str(self.get_location()[0])+","+str(self.get_location()[0]) + ')'))
                model.remove(self)
        return check_set
    
    def display(self, the_canvas):
        width,height = self.get_dimension()
        the_canvas.create_oval(self._x-width/2, self._y-height/2, self._x+width/2, self._y+height/2,fill = self.color)

    def contains(self, xy):
        return self.distance(xy) <= self.get_dimension()[0]/2    