from collections import Counter
from sense_emu import SenseHat
from time import sleep

def main():
    
    total_miles = 0
    miles = int(input("Enter the number of miles"))
    while miles != 0:
        total_miles += miles
        miles = int(input("Enter the number of miles"))
    print("You drove {:d} miles".format(total_miles))
    sense = SenseHat()
    sleep(1)
    initial_humidity = sense.get_humidity()
    current_humidity = initial_humidity
    while current_humidity <= (initial_humidity + 3):
        print("humidity: {:.2f}%".format(current_humidity))
        current_humidity = sense.get_humidity()
        sleep(0.1)
    print("humidty inscreased by 3% or more ")
    print("seniten ands counter control")
    sleep(5)
    count = 1
    
    initial_humidity = sense.get_humidity()
    current_humidity = initial_humidity
    while ((current_humidity <= (initial_humidity + 3)) and count<=100):
        print("humidity is {:.2f}%".format(current_humidity))
        if current_humidity > (initial_humidity + 3):
            print("Humidity has increased by 3% more")
        else:
            print("We tested the humidity enough")
    main()
    