# A Hunter is derived from a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.distance1 = 200
        self.randomize_angle()
    
    def update(self, model):
        hunted_set = Pulsator.update(self, model)
        def locations(i):
            return self.distance(i.get_location()) <= self.distance1
        prey_found = model.find(lambda x: isinstance(x, Prey) and locations(x))
        prey_list = []
        if prey_found:
            for i in prey_found:
                prey_list.append(((self.distance(i.get_location())),i))
                sorted_prey_list = sorted(prey_list,key = lambda x: x[0])
                target = sorted_prey_list[0][1]
                hunterx,huntery = self.get_location()
                preyx,preyy = target.get_location()
                self.set_angle(atan2(preyy-huntery,preyx-hunterx))
        self.move()
        return hunted_set
