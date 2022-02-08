#display_message.py
#Tyler Mears
from sense_hat import SenseHat

sense = SenseHat()
help(sense)
sense.show_message("python with raspberry pi", text_colour =
                   [255,0,255], back_colour = [0,255,255],
                   scroll_speed = 0.05)
sense.clear()