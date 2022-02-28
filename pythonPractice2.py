#this program will decide whether or not a number is divisible by 2

# saying hi to the user
print("hello user,")
# telling the user what the program does
print("This program will request a number f")
# getting user input. Asking user for a number
user_number = int(input("Please enter a number: "))
# using the python modulus operator which will return a 0 if is even.
math = user_number % 2
#using the math variable which will return a 0 is even
# because i know this i make an if else statement
# if math is 0 then we know is even and print is even
# else not even print the selected number is odd
if math == 0:
    print("Your selected number is even")
else: print("Your selected number is odd")