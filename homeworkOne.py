from sense_hat import SenseHat
import math
from time import sleep
sense = SenseHat()
sense.clear()
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
limegreen = (50,205,50)
black = (0,0,0)
sense.show_message("Tyler Mears", text_colour=red, back_colour=blue, scroll_speed=0.04)
sense.clear()
pressure = sense.get_pressure()
sense.show_message(f'{pressure:.3f}', text_colour=limegreen, back_colour=black, scroll_speed=0.5)
psi = pressure / 6894.75729
sense.show_message(f'{pressure:12.4f}', text_colour=yellow, back_colour=black, scroll_speed=0.5)
r = (255,0,0)
o = (255,128,0)
y = (255,255,0)
g = (0,255,0)
c = (0,255,255)
b = (0,0,255)
p = (255,0,255)
n = (255,128,128)
w = (255,255,255)
k = (0,0,0)
hwexample = [
w,k,k,k,k,k,k,r,
w,k,b,k,k,r,k,g,
w,k,k,k,r,k,k,b,
w,y,k,r,k,k,k,y,
w,k,k,g,g,k,k,k,
p,g,k,k,k,k,k,k,
b,k,k,k,k,k,k,k,
y,k,k,k,k,k,k,k,
]
sense.set_pixels(hwexample)
sleep(10)
r = (255,0,0)
o = (255,128,0)
y = (255,255,0)
g = (0,255,0)
c = (0,255,255)
b = (0,0,255)
p = (255,0,255)
n = (255,128,128)
w = (255,255,255)
k = (0,0,0)
hwexample2 = [
w,k,k,k,k,k,k,r,
w,k,b,k,k,r,k,g,
w,k,k,k,r,k,k,b,
w,y,k,r,k,k,k,y,
w,k,k,g,g,k,k,k,
p,g,k,k,k,k,k,k,
b,k,k,k,k,k,k,k,
y,k,k,k,k,k,k,k,
]
sense.set_pixels(hwexample2)
for y in range(8):
colour = hwexample2[y]
for x in range(8):
sense.set_pixel(x, y, colour)
sleep(0.2)
creeper = [
g,g,g,g,g,g,g,g,
g,b,b,g,g,b,b,g,
g,b,b,g,g,b,b,g,
g,g,g,b,b,g,g,g,
g,g,b,b,b,b,g,g,
g,g,r,r,r,r,g,g,
g,g,r,g,g,r,g,g,
g,g,r,g,g,r,g,g,
]
sense.set_pixels(creeper)