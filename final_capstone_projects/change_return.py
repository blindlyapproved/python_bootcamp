def change_return():

    price = float(input("Item price: "))

    amount_paid = float(input("Amount of money paid: "))

    one_dollar = 1.00
    quarter = 0.25
    dime = 0.10
    nickel = 0.5
    penny = 0.01

    changeTypes = {one_dollar:0,quarter:0,dime:0, nickel:0, penny:0}

    change = amount_paid - price

    if amount_paid < price:
        print("Not enough $$$")

    for changeType in changeTypes:
        numAmount = max(0, change // changeType)
        change -= numAmount * changeType
        changeTypes[changeType] = int(numAmount)

    print(changeTypes)


change_return()