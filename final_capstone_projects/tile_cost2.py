# How much tile for your money

def tile_cost():

    cost = float(input("What's your available budget? "))

    cost_per_sqm = 10.00

    surface_for_budget = cost / cost_per_sqm

    print(f"With your budget of ${cost} you can lay {surface_for_budget} of squaremeters")

tile_cost()