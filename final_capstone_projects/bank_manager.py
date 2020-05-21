class Account:

    def __init__(self, id, balance):

        self.id = id
        self.balance = balance

    def get_id(self):
        return self.id

    def get_balance(self):
        return self.balance

    def desposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount
            

def main():

    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

    while True:

        print("\nHello, welcome to ABC Bank")

        id = int(input("\nEnter your PIN please: "))

        while id <1000 or id >9999:
            id = int(input("\n Incorrect PIN, try again: "))
    
        while True:

            print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit")

            selection = int(input("\nPlease make your choice: "))

            for acc in accounts:
                if acc.get_id() == id:
                    account_object = acc
                    break

            if selection == 1:
                print("\nYour balance is: $" + str(account_object.get_balance()) + " ")

            elif selection == 2:
                amt = float(input("\nEnter amount to withdraw: "))
                verify_withdraw = input("Please verify this is the correct amount. Yes/No: $" +str(amt) + "  ")

                if verify_withdraw == "Yes":
                    print("Withdrawing...")
                else:
                    break

                if amt < account_object.get_balance():
                    account_object.withdrawal(amt)
                    print("\nNew Balance: $" + str(account_object.get_balance()) + "")
                else:
                    print("You have exceeded your balance. Retry with lower withdrawl amount")

            elif selection == 3:
                amt = float(input("\n Enter amount to deposit: "))

                verify_deposit = input("Please verify this is the correct amount. Yes/No: $" + str(amt) + "  ")

                if verify_deposit == "Yes":
                    account_object.desposit(amt)
                    print(type(account_object))
                    print("Deposit successful.")
                else:
                    break

            elif selection == 4: 
                print("\nThank you for choosing ABC")
                exit()

            else:
                print("Invalid choice")
main()