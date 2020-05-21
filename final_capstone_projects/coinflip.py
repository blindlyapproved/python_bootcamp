import random

def coinflip():

    score_heads = 0
    score_tails = 0
    
    while True:

        print("\nWelcome to Coin flip")

        tossed_coin = random.randint(1,2)

        if tossed_coin == 1:
            score_heads +=1
            print("\nHeads won")

        if tossed_coin == 2:
            score_tails +=1
            print("\nTails won")

        print(f"\nHeads score: {score_heads}")
        print(f"Tails score: {score_tails}")

        again = input("\nWant to play again? Yes or No:   ").lower()

        if again == "y":
            continue
        else:
            print("\nThanks for playing.")
            print("\nFinal score:")
            print(f"Heads score: {score_heads}")
            print(f"Tails score: {score_tails}")
            print("\n")
            exit()

coinflip()