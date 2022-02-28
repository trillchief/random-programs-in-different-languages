#Tyler Mears
#2/25/2022

pi_cost = 35

pi_name = input(print("Name of pi please: "))
pi_buy = int(input(print("How many pi's do you want to buy?:")))

if pi_name == "ZeroW2":
    pi_cost = 15
    print(pi_cost)
elif pi_name == "ZeroH" or pi_name == "ZeroW":
    pi_cost =10
    print(pi_cost)
elif pi_name == "400":
    pi_cost = 70
    print(pi_cost)
elif pi_name == "4":
    pi_cost = 45
    print(pi_cost)

if pi_buy >= 1 and pi_buy <= 10:
    pi_price = pi_buy * pi_cost
    print(pi_price)
elif pi_buy >= 10 and pi_buy <= 11:
    pi_price = pi_buy * (pi_cost-0.5)
    print(pi_price)
elif pi_buy >= 11 and pi_buy <= 50:
    pi_price = pi_buy * (pi_cost-0.75)
    print(pi_price)
else:
    pi_price = pi_buy * (pi_cost-1)
    print(pi_price)
