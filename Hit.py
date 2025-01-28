import random

suits = ['Clubs','Diamonds','Hearts','Spades']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

rank = random.choice(ranks)
suit = random.choice(suits)
deck = ranks + suits

n = len(deck)
for i in range(n):
    r = random.randrange(0, i + 1)
    temp = deck[r]
    deck[r]=deck[i]
    deck[i] = temp
print(deck)