# Instructions
# Only a computer dealer and human player
# Create representation of card deck in OOP
# Player places a bet - they have a bank roll with a attr for that bank roll
# Player starts with 2 cards face up
# Dealer starts with 1 card face up and 1 card face down
# Player goes first
# Player goal is to get closer to 21: total value is sum of current player card
# Player can hit (Receive another card)
# Player can stay (Stop receiving another card)
# If player is still under 21, dealer then hits until they beat the player or bust
# bust == over 21
# If player keeps hitting over 21 == Bust == Lost bet
# Human player goes - stay (19) - dealer goes and sum is higher and < 21 then dealer wins
# Dealer keeps hitting: higher than player, 21 or bust
# Face cards == value 10
# Aces can count as either 1 or 11

import random

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two" :2, "Three" :3, "Four" :4, "Five" :5, "Six" :6, "Seven" :7, "Eight" :8, "Nine" :9, "Ten" :10, "Jack" :10, "Queen" :10, "King" :10, "Ace" :11}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + "of " + self.suit

class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        full_deck = ""
        for card in self.deck:
            full_deck += "\n" + card.__str__()
        return "This is the deck" + full_deck


    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffle()
print(test_deck)

single_card = test_deck.deal_card()
print(single_card)

    
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.hand = []

#     def draw(self, deck):
#         self.hand.append(deck.drawCard())
#         return self

#     def showHand(self):
#         for card in self.hand:
#             card.show()

# deck = Deck()
# deck.shuffle()

# luuk = Player("Luuk")
# luuk.draw(deck)
# luuk.showHand()

class Dealer:
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

class Player:

    def __init__(self, player, balance):

        self.player =  player
        self.balance = balance
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def player_wins(self, won_amount):
        self.balance = self.balance + won_amount
        print("Congratiulations you won ${}".format(won_amount))

    def player_loses(self, los_amount):

        self.balance = self.balance - los_amount
        print("You lost ${}".format(los_amount))

    def add_to_player_balance(self, deposit_amount):

        self.balance = self.balance + deposit_amount

    def __str__(self):

        return f"The player is {self.player} and the balance is {self.balance}"

    def place_bet(self, bet):

        if self.balance >= bet:
            self.balance = self.balance - bet
            print("You placed a bet of ${} and your remaining balance is ${}".format(bet, self.balance))

        else:
            print("Sorry, you can't place a bet that is higher than your balance, place a lower bet.")


    def get_card(self, card):
        pass

    def hit_card(self, card):
        pass

    def hit_again(self, card):
        pass

    def make_up_balance(self, won_amount, los_amount, balance):
        pass



# PAYMENT PROCESS, INITIALIZE THE PLAYER
player1 = Player("Luuk", 100)
print(player1)

# PAYMENT PROCESS, PLAYER WINS (BJ OR > THAN BANK)
player1.player_wins(100)
print(player1)

# PAYMENT PROCESS, PLAYER LOSES (BUST, < THAN BANK OR BANK HAS BJ)
player1.player_loses(100)
print(player1)

# PAYMENT PROCESS, IF BALANCE REACHES 0, PLAYER CAN MAKE DEPOSIT
player1.add_to_player_balance(99)
print(player1)

# PAYMENT PROCESS, PLAYER CANNOT MAKE BET HIGHER THAN BALANCE
player1.place_bet(20)
# def player_win_check(self):
#     if Player.showHand(1) == 21 or Player.showHand(1) >= Dealer.showHand(1):
#         return "You won"

# def bust():
#     return Player.showHand(1) or Dealer.showHand(1) >= 21