# Poker game - 5 card stud

from random import shuffle
from copy import deepcopy


class Deck:
    card_list = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self.cards = []

    def build_deck(self, num_decks=1):
        for n in range(num_decks):
            for c in self.card_list:
                for s in self.suit_list:
                    if c is not None:
                        self.cards.append([self.card_list.index(c), c, s])
        shuffle(self.cards)


class Player:
    player_list = []
    num_cards_dealt = 5

    def __init__(self):
        self.hand = []
        self.high_cards = []
        self.pair_1 = []
        self.pair_2 = []
        self.two_pair = []
        self.three_kind = []
        self.straight = []
        self.flush = []
        self.full_house = []
        self.four_kind = []
        self.straight_flush = []
        self.royal_straight_flush = []

    def deal_card(self):
        card = deck.cards.pop()
        self.hand.append(card)

    def sort_cards(self):
        self.hand.sort(reverse=True)

    def of_kind_4(self):
        for i in range(2):
            if self.hand[i][0] == self.hand[i+1][0] and self.hand[i][0] == self.hand[i+2][0]\
                    and self.hand[i][0] == self.hand[i+3][0]:
                self.four_kind.append(self.hand[i])
                self.four_kind.append(self.hand[i + 1])
                self.four_kind.append(self.hand[i + 2])
                self.four_kind.append(self.hand[i + 3])

    def of_kind_3(self):
        if self.four_kind == []:
            for i in range(3):
                if self.hand[i][0] == self.hand[i+1][0] and self.hand[i][0] == self.hand[i+2][0]:
                    self.three_kind.append(self.hand[i])
                    self.three_kind.append(self.hand[i + 1])
                    self.three_kind.append(self.hand[i + 2])
                    return

    def of_kind_2(self):
        if self.four_kind != []:
            return
        elif self.three_kind == []:  # checks for 2 pair
            for i in range(4):
                if self.pair_1 == [] and self.hand[i][0] == self.hand[i+1][0]:
                    self.pair_1.append(self.hand[i])
                    self.pair_1.append(self.hand[i+1])
                elif self.pair_1 != [] and self.hand[i][0] != self.pair_1[0][0]\
                        and self.hand[i][0] == self.hand[i+1][0]:
                    self.pair_2.append(self.hand[i])
                    self.pair_2.append(self.hand[i+1])
            return
        else:  # checks for 1 pair
            for i in range(4):
                if self.pair_1 == [] and self.hand[i][0] == self.hand[i+1][0]\
                        and self.hand[i][0] != self.three_kind[0][0]:
                    self.pair_1.append(self.hand[i])
                    self.pair_1.append(self.hand[i+1])

    def of_pair_1(self):
        pass

    def of_pair_2(self):
        pass

    def of_straight(self):
        if self.hand[-5][0] > 5:
            if self.hand[-5][0] - 1 == self.hand[-4][0] and \
             self.hand[-5][0] - 2 == self.hand[-3][0] and \
             self.hand[-5][0] - 3 == self.hand[-2][0] and \
             self.hand[-5][0] - 4 == self.hand[-1][0]:
                self.straight.append(self.hand[-1])
                self.straight.append(self.hand[-2])
                self.straight.append(self.hand[-3])
                self.straight.append(self.hand[-4])
                self.straight.append(self.hand[-5])

    def of_flush(self):
        self.suit_check = self.hand[0][2]
        self.count = 0
        for i in self.hand:
            if i[2] == self.suit_check:
                self.count += 1
        if self.count == 5:
            self.flush = self.hand

    def of_straight_flush(self):
        if self.straight != [] and self.flush != []:
            self.straight_flush = self.straight

    def of_royal_straight_flush(self):
        if self.straight != [] and self.flush != [] and self.hand[0][1] == 'Ace':
            self.royal_straight_flush = self.straight

    def of_full_house(self):
        if self.three_kind != [] and self.pair_1 != []:
            self.full_house.append(self.three_kind[0])
            self.full_house.append(self.three_kind[1])
            self.full_house.append(self.three_kind[2])
            self.full_house.append(self.pair_1[0])
            self.full_house.append(self.pair_1[1])

    def of_two_pair(self):
        if self.pair_1 != [] and self.pair_2 != []:
            self.two_pair.append(self.pair_1[0])
            self.two_pair.append(self.pair_1[1])
            self.two_pair.append(self.pair_2[0])
            self.two_pair.append(self.pair_2[1])

    def of_best_play(self):

        if self.royal_straight_flush != []:
            self.best_play = 100
            self.best_play_name = "a Royal Straight Flush"
        elif self.straight_flush != []:
            self.best_play = 90
            self.best_play_name = "a Straight Flush"
        elif self.four_kind != []:
            self.best_play = 80
            self.best_play_name = "Four of a Kind"
        elif self.full_house != []:
            self.best_play = 70
            self.best_play_name = "a Full House"
        elif self.flush != []:
            self.best_play = 60
            self.best_play_name = "a Flush"
        elif self.straight != []:
            self.best_play = 50
            self.best_play_name = "a Straight"
        elif self.three_kind != []:
            self.best_play = 40
            self.best_play_name = "3 of a Kind"
        elif self.two_pair != []:
            self.best_play = 30
            self.best_play_name = "2 Pair"
        elif self.pair_1 != []:
            self.best_play = 20
            self.best_play_name = "1 Pair"
        else:
            self.best_play = 10
            self.best_play_name = "a High Card"

    def of_high_cards(self):
        self.high_cards = deepcopy(self.hand)

        if self.royal_straight_flush != []:
            for item in self.royal_straight_flush:
                self.high_cards.remove(item)
        elif self.straight_flush != []:
            for item in self.straight_flush:
                self.high_cards.remove(item)
        elif self.four_kind != []:
            for item in self.four_kind:
                self.high_cards.remove(item)
        elif self.full_house != []:
            for item in self.full_house:
                self.high_cards.remove(item)
        elif self.flush != []:
            for item in self.flush:
                self.high_cards.remove(item)
        elif self.straight != []:
            for item in self.straight:
                self.high_cards.remove(item)
        elif self.three_kind != []:
            for item in self.three_kind:
                self.high_cards.remove(item)
        elif self.two_pair != []:
            for item in self.two_pair:
                self.high_cards.remove(item)
        elif self.pair_1 != []:
            for item in self.pair_1:
                self.high_cards.remove(item)
        else:
            pass  # all high cards will be evaluated


# decide winner

def decide_winner():
    if p1.best_play > p2.best_play:
        print("Player 1 wins with", p1.best_play_name)
    elif p2.best_play > p1.best_play:
        print("Player 2 wins with", p2.best_play_name)
    else:
        print("Tie Breaker!!!")

        if p1.best_play == 100 and p2.best_play == 100:  # royal straight flush
            if p1.straight[0][0] > p2.straight[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.straight[0][0] < p2.straight[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 90 and p2.best_play == 90:  # straight flush
            if p1.straight[0][0] > p2.straight[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.straight[0][0] < p2.straight[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 80 and p2.best_play == 80:  # four of a kind
            if p1.four_kind[0][0] > p2.four_kind[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.four_kind[0][0] < p2.four_kind[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                if p1.high_cards[0][0] > p2.high_cards[0][0]:
                    print("Player 1 wins with", p1.best_play_name, "and High Card tie breaker")
                if p1.high_cards[0][0] < p2.high_cards[0][0]:
                    print("Player 2 wins with", p2.best_play_name, "and High Card tie breaker")
                else:
                    print("Tie Game - Split the Pot")

        if p1.best_play == 70 and p2.best_play == 70:  # full house
            if p1.three_kind[0][0] > p2.three_kind[0][0]:
                print("Player 1 wins with", p1.best_play_name, "and highest 3 of a kind")
            elif p1.three_kind[0][0] < p2.three_kind[0][0]:
                print("Player 2 wins with", p2.best_play_name, "and highest 3 of a kind")
            elif p1.three_kind[0][0] == p2.three_kind[0][0]:
                if p1.pair_1[0][0] > p2.pair_1[0][0]:
                    print("Player 1 wins with", p1.best_play_name, "and highest pair")
                elif p1.pair_1[0][0] < p2.pair_1[0][0]:
                    print("Player 2 wins with", p2.best_play_name, "and highest pair")
                else:
                    print("Tie Game - Split the Pot")

        if p1.best_play == 60 and p2.best_play == 60:  # flush
            if p1.flush[0][0] > p2.flush[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.flush[0][0] < p2.flush[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 50 and p2.best_play == 50:  # straight
            if p1.straight[0][0] > p2.straight[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.straight[0][0] < p2.straight[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 40 and p2.best_play == 40:  # three of a kind
            if p1.three_kind[0][0] > p2.three_kind[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.three_kind[0][0] < p2.three_kind[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            elif p1.high_cards[0][0] > p2.high_cards[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.high_cards[0][0] < p2.high_cards[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            elif p1.high_cards[1][0] < p2.high_cards[1][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.high_cards[1][0] > p2.high_cards[1][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 30 and p2.best_play == 30:  # two pair
            if p1.pair_1[0][0] > p2.pair_1[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.pair_1[0][0] < p2.pair_1[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            elif p1.pair_2[0][0] > p2.pair_2[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.pair_2[0][0] < p2.pair_2[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            elif p1.high_cards[0][0] > p2.high_cards[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.high_cards[0][0] < p2.high_cards[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 20 and p2.best_play == 20:  # one pair
            if p1.pair_1[0][0] > p2.pair_1[0][0]:
                print("Player 1 wins with", p1.best_play_name)
            elif p1.pair_1[0][0] < p2.pair_1[0][0]:
                print("Player 2 wins with", p2.best_play_name)
            elif p1.pair_1[0][0] == p2.pair_1[0][0]:
                for i in range(3):
                    if p1.high_cards[i][0] > p2.high_cards[i][0]:
                        print("Player 1 wins with", p1.best_play_name)
                        return
                    if p1.high_cards[i][0] < p2.high_cards[i][0]:
                        print("Player 2 wins with", p2.best_play_name)
                        return
            else:
                print("Tie Game - Split the Pot")

        if p1.best_play == 10 and p2.best_play == 10:  # high card
            for i in range(5):
                    if p1.high_cards[i][0] > p2.high_cards[i][0]:
                        print("Player 1 wins with", p1.best_play_name, p1.high_cards[i])
                        return
                    if p1.high_cards[i][0] < p2.high_cards[i][0]:
                        print("Player 2 wins with", p2.best_play_name, p2.high_cards[i])
                        return
            else:
                print("Tie Game - Split the Pot")


def play_game():

    # deal cards to players
    for i in range(Player.num_cards_dealt):
        p1.deal_card()
        p2.deal_card()

    # sort cards
    p1.sort_cards()
    p2.sort_cards()

    # calculate players highest score

    p1.of_kind_4()
    p1.of_kind_3()
    p1.of_kind_2()
    p1.of_two_pair()
    p1.of_full_house()
    p1.of_straight()
    p1.of_flush()
    p1.of_straight_flush()
    p1.of_royal_straight_flush()
    p1.of_high_cards()
    p1.of_best_play()

    p2.of_kind_4()
    p2.of_kind_3()
    p2.of_kind_2()
    p2.of_two_pair()
    p2.of_full_house()
    p2.of_straight()
    p2.of_flush()
    p2.of_straight_flush()
    p2.of_royal_straight_flush()
    p2.of_high_cards()
    p2.of_best_play()

    # Testing

    print("P1 Hand:", p1.hand)
    print("P2 Hand:", p2.hand)

    print("P1 Best Play:", p1.best_play_name)
    print("P2 Best Play:", p2.best_play_name)

    decide_winner()


number_of_games = range(1)

for games in number_of_games:

    # initialize the deck
    deck = Deck()
    deck.build_deck()

    # initialize players
    p1 = Player()
    p2 = Player()

    play_game()

    with open("log.txt", "a") as log:
        log.write(p1.best_play_name)
        log.write("\n")
        log.write(p2.best_play_name)
        log.write("\n")
