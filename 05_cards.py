from random import shuffle
suits = ["♥", "♦", "♣", "♠"]
deck = []

for suit in suits:
    for x in range(1, 14):
        if x == 11:
            deck.append("J" + suit)
        elif x == 12:
            deck.append("Q" + suit)
        elif x == 13:
            deck.append("K" + suit)
        elif x == 1:
            deck.append("A" + suit)
        else:
            deck.append(str(x) + suit)

shuffle(deck)

player1 = deck[0:26]
player2 = deck[26:52]
print(deck)
print(player1)
print(player2)
