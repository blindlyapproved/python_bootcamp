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

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range (1, 14):
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            res = random.randint(0, i)
            self.cards[i], self.cards[res] = self.cards[res], self.cards[i]

    def drawCard(self):
        return self.cards.pop(-51)

    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

deck = Deck()
deck.shuffle()

luuk = Player("Luuk")
luuk.draw(deck)
luuk.showHand()



class PlayerMoney():

    def __init__(self, player, balance=100):

        self.player = player
        self.balance = balance

    def player_wins(self, won_amount):

        self.balance = self.balance + won_amount
        print("Congratiulations you won ${}".format(won_amount))

    def player_loses(self, los_amount):

        self.balance = self.balance - los_amount
        print("You lost ${}".format(los_amount))

    def add_to_player_balance(self, deposit_amount):

        self.balance = self.balance + deposit_amount