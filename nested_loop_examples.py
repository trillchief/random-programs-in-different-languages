from sense_emu import SenseHat
from time import sleep

def main():
    for i in range(1, 7):
        for j in range(0, 11, 2):
            print("i = {:d}".format(i, j))
    sense = SenseHat()
    for row in range(0, 8):
        for col in range(0,8):
            sense.set_pixel(row, 0, 0, 255)
            sleep(0.2)
    
    sleep(5)
    sense.clear()
    day_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    total_hours = 0
    for emp in range(1,4):
        for day in day_tuple:
            hour = int(input("Enter the hours worked in {:s} for employee {:d}".format(day, emp)))
            total_hours += hour
    print("Total hours worked for all employees is {:d}".format(total_hours))
            
    
main()
