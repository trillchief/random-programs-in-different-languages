# this program will obtain user information
# it will obtain name, age, and current year
# then will tell the user in what year they will turn 100 years old


user_name = input(
    "What is your name, sir? \nPlease enter here at your own risk: ")  # asking user for their name

# obtaining users age
user_age = (input("Please enter your age numerically: "))

current_year = (input("Please enter your current year: ")
                )  # obtaining the current year
math_age = int(user_age)  # converting users age to int
math_current_year = int(current_year)  # converting the current year to int
math = 100 - math_age  # 100 - the users age
# 100 - the users age + the current year which will be the answer we are looking for
calculated_year = math + math_current_year

# converting the current year to a string so that it can be concatinated
calculatedYear = str(calculated_year)

# printing users name and age and telling them in which year they will be 100 years old
print(user_name + ", you are currently " + user_age +
      " years old, and will turn 100 years old in the year: " + calculatedYear)
