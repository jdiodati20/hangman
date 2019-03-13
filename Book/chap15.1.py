from random import shuffle

class card:
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        a = (self.values[self.value] + " of " + self.suits[self.suit])
        return(a)

    def __lt__(self, card2):
        if self.value > card2.value:
            return True
        elif self.value < card2.value:
            return False
        else:
            return "It is a tie"


class deck:
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class player:
    def __init__(self, name, Deck):
        self.hand = Deck
        self.name = name


class game:
    def __init__(self):
        player1 = input("Player One: ")
        player2 = input("Player Two: ")
        Deck = deck()
        d1 = Deck.cards[:len(Deck.cards) // 2]
        d2 = Deck.cards[len(Deck.cards) // 2:]
        self.p1 = player(player1, d1)
        self.p2 = player(player2, d2)

    def roundWinner(self, winner):
        print("{} wins this round.".format(winner))

    def round1(self, p1c, p2c):
        result = "{} drew a {}"
        result1 = result.format(self.p1.name, p1c)
        result2 = result.format(self.p2.name, p2c)
        print(result1)
        print(result2)

    def totalWinner(self):
        if len(self.p1.hand) == 0:
            return self.p2.name
        elif len(self.p2.hand) == 0:
            return self.p1.name
        return "Error"

    def whichIsSmaller(self):
        if(len(self.p1.hand) > len(self.p2.hand)):
            return int(len(self.p2.hand))
        elif(len(self.p1.hand) < len(self.p2.hand)):
            return int(len(self.p1.hand))
        else:
            return 26

    def isTie(self, card1, card2):
        length = self.whichIsSmaller()
        if (length < 3):
            temp1 = self.p1.hand[:length - 1]
            temp2 = self.p2.hand[:length - 1]
            self.p1.hand = self.p1.hand[length - 1:]
            self.p2.hand = self.p2.hand[length - 1:]
            p1c = self.p1.hand.pop(0)
            p2c = self.p2.hand.pop(0)
            self.round1(p1c, p2c)
            if p1c.value > p2c.value:
                self.p1.hand.extend(temp1)
                self.p1.hand.extend(temp2)
                self.p1.hand.append(p1c)
                self.p1.hand.append(p2c)
                self.p1.hand.append(card1)
                self.p1.hand.append(card2)
                print("{} wins this war!".format(self.p1.name))
            elif p1c.value < p2c.value:
                self.p2.hand.extend(temp1)
                self.p2.hand.extend(temp2)
                self.p2.hand.append(p1c)
                self.p2.hand.append(p2c)
                self.p2.hand.append(card1)
                self.p2.hand.append(card2)
                print("{} wins this war".format(self.p2.name))
            else:
                self.p1.hand.extend(temp1)
                self.p2.hand.extend(temp2)
                self.p1.hand.append(p1c)
                self.p2.hand.append(p2c)
                self.p1.hand.append(card1)
                self.p2.hand.append(card2)
                print("This war is a tie")
        else:
            temp1 = self.p1.hand[:3]
            temp2 = self.p2.hand[:3]
            self.p1.hand = self.p1.hand[3:]
            self.p2.hand = self.p2.hand[3:]
            p1c = self.p1.hand.pop(0)
            p2c = self.p2.hand.pop(0)
            self.round1(p1c, p2c)
            if p1c.value > p2c.value:
                self.p1.hand.extend(temp1)
                self.p1.hand.extend(temp2)
                self.p1.hand.append(p1c)
                self.p1.hand.append(p2c)
                self.p1.hand.append(card1)
                self.p1.hand.append(card2)
                print("{} wins this war!".format(self.p1.name))
            elif p1c.value < p2c.value:
                self.p2.hand.extend(temp1)
                self.p2.hand.extend(temp2)
                self.p2.hand.append(p1c)
                self.p2.hand.append(p2c)
                self.p2.hand.append(card1)
                self.p2.hand.append(card2)
                print("{} wins this war".format(self.p2.name))
            else:
                self.p1.hand.extend(temp1)
                self.p2.hand.extend(temp2)
                self.p1.hand.append(p1c)
                self.p2.hand.append(p2c)
                self.p1.hand.append(card1)
                self.p2.hand.append(card2)
                print("This war is a tie")


    def playGame(self):
        print("Welcome to war \nLet us begin!")
        print("________")
        while (len(self.p1.hand) and len(self.p2.hand)) > 0:
            start = input("Press q to quit, and any other key to continue")
            if start == "q":
                break
            print("Cards in {}'s hand: {} cards".format(self.p1.name, len(self.p1.hand)))
            print("Cards in {}'s hand: {} cards".format(self.p2.name, len(self.p2.hand)))
            print()
            p1c = self.p1.hand.pop(0)
            p2c = self.p2.hand.pop(0)
            self.round1(p1c, p2c)
            print()
            if (p1c.value > p2c.value):
                self.p1.hand.append(p1c)
                self.p1.hand.append(p2c)
                self.roundWinner(self.p1.name)
            elif (p1c.value < p2c.value):
                self.p2.hand.append(p2c)
                self.p2.hand.append(p1c)
                self.roundWinner(self.p2.name)
            elif (p1c.value == p2c.value):
                print("It is a war")
                self.isTie(p1c, p2c)
            print("_______")
            for i in range(3):
                print()
        print("Cards in {}'s hand: {} cards".format(self.p1.name, len(self.p1.hand)))
        print("Cards in {}'s hand: {} cards".format(self.p2.name, len(self.p2.hand)))
        print("{} is the winner!".format(self.totalWinner()))
        
total = game()
total.playGame()
