# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey):
    
    speed = 5
    angle = 0
        
    def __init__(self,x,y):
        self._image = PhotoImage(file='ufo.gif')
        Prey.__init__(self,x,y,self._image.width(),self._image.height(),Floater.angle,Floater.speed) 
        self.randomize_angle()     

    def update(self,*model):
        if random.randint(1,10) <= 3:
            speed_difference = random.uniform(-0.5, 0.5)
            if self.get_speed() + speed_difference >= 3 and self.get_speed() + speed_difference <= 7:
                self.set_speed(self.get_speed() + speed_difference)
            self.set_angle(self.get_angle() + random.uniform(-0.5, 0.5))            
        self.move()
        return set()
    
    def display(self,canvas):
        canvas.create_image(*self.get_location(),image=self._image)