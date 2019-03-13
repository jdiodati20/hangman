from random import shuffle

class card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if (self.suit > c2.suit):
                return True
        else:
            return False
        return False
    def __repr__(self):
        return(self.values[self.value] + " of " + self.suits[self.suit])

class deck:
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return()
        return self.cards.pop()

class player:
    def __init__(self, name):
        self.wins = 0
        self.name = name
        self.card = None

class game:
    def __init__(self):
        name1 = input("Player One Name: ")
        name2 = input("Player Two Name: ")
        self.deck = deck()
        self.p1 = player(name1)
        self.p2 = player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
        print("____")

    def draw(self, p1, p2, p1c, p2c):
        result1 = "{} drew {}"
        result2 = "{} drew {}"
        result1 = result1.format(p1, p1c)
        result2 = result2.format(p2, p2c)
        print(result1)
        print(result2)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        else:
            return p2.name

    def play_game(self):
        cards = self.deck.cards
        print("Let us begin!")
        while len(cards) >=  2:
            start = "q to quit. Any key to begin."
            begin = input(start)
            if begin == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p2n, p1c, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        win1 = self.winner(self.p1, self.p2)
        tally = self.p2.wins
        if (win1 is self.p1.name):
            tally = self.p1.wins
        print("War is over.  {} is the winner with {} wins!".format(win1, tally))
play = game()
play.play_game()
