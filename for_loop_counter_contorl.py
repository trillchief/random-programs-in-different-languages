from sense_emu import SenseHat
from time import sleep

def main():
    for count in range(11):
        print(count)
    for count in range(5, 10):
        print(count)
    for i in range(0, 21, 2):
        print(i)
    for j in range(30, 12, -3):
        print(j)
    sense = SenseHat()
    for count_down in range(9, -1, -1):
        sense.show_letter(chr(count_down = 48), back_colour =
                          [200, 200, 0], text_colour = [0, 0, 255])
        sleep(1)
    sense.show_message("Blast off!", text_colour = [255, 0, 0, 0],
                       back_colour = [0, 0, 0,], scroll_speed = 0.1)
    
    my_color = [255, 255, 200]
    
    for index in range(len(my_color)):
        print(my_color[index])
    
    for color in my_color:
        print(c)
    
    class_list = ["cop 1030", "cnt 2402", "cnt 2000", "cop 122"]
    for c in class_list:
        print(c)
    
main()