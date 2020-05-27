def tax_calc():
    print("Welcome to tax calculator. Insert your cost and local tax rate and we do the rest.")
    price = float(input("Please insert the price without tax: "))
    get_tax_rate = float(input("What is your local tax rate (%): "))

    tax_rate = get_tax_rate / 100

    price_with_tax = price * tax_rate + price

    print(f"The price of your product including tax is {price_with_tax}")

tax_calc()