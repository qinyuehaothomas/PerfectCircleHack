import keyboard
from pyautogui import *
from math import sin,cos,radians

r=300
edg=5
x,y=size()
x/=2
y=(y-34.75-13)/2
def listener(key):
    if key.name=="Q" or key.name=='q':
        # print(position())
        for i in range(0,1+edg):
            offx=x+ cos(radians(360.0*(i/edg)))*r
            offy=y+ sin(radians(360.0*(i/edg)))*r
            # print(offx,offy)
            if(i>0):
                moveTo(offx,offy)
            else:
                moveTo(offx,offy)
                mouseDown()
        mouseUp()
if __name__ == "__main__":
    keyboard.on_press(listener)
    keyboard.wait('esc')  # Wait for 'esc' key press to quit
