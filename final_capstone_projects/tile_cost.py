def cost_tile():

    price_per_sqm = 10

    w = float(input("What is the width of your floor? "))
    h = float(input("And what's the height? "))

    customer_cost = w * h * price_per_sqm

    print("The cost for this floor would be $",customer_cost)

cost_tile()



