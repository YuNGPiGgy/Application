import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running         = False
one_cycle       = False
cycle_count     = 0
simultons       = set()
clicked_button  = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, one_cycle
    running         = False
    one_cycle       = False
    cycle_count     = 0
    simultons       = set()

#start running the simulation
def start ():
    global running
    running     = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running     = False


#step just one update in the simulation
def step ():
    global running, one_cycle
    running     = True
    one_cycle   = True

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked_button
    clicked_button = kind

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global simultons, clicked_button
    if clicked_button == 'remove'.title():
            objects = find(lambda j: j.contains((x,y)))
            for i in objects:
                simultons.remove(i)
    else:
        simultons.add(eval(clicked_button + '(' + str(x) + ',' + str(y) + ')'))

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for i in simultons:
        if p(i):
            result.add(i)    
    return result


#call update for every simulton in the simulation
def update_all():
    global running, one_cycle, cycle_count, world
    if running:
        cycle_count += 1

        original_simultons = set(simultons)
        for s in original_simultons:
            if s in simultons:
                s.update(model) 
        if one_cycle:
            running = False
            one_cycle = False


#delete from the canvas every simulton in the simulation; then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    for j in simultons:
        j.display(controller.the_canvas)
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(simultons))+" simultons")
