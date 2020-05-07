class Account():

    def __init__(self, customer_id, balance=0):

        self.customer_id = customer_id
        self.balance = balance

class CheckingAccount(Account):

    def __init__(self, customer_id, deposit_amount, withdrawal_amount):

        self.deposit_amount = deposit_amount
        self.withdrawal_amoutn = withdrawal_amount
        
    def deposit(self, balance, deposit_amount):

        self.balance = self.balance + deposit_amount
        print("You deposited ${} to your account".format(deposit_amount))
        print("Your total balance is now ${}".format(balance))
