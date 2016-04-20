from deck import Deck
from player import Player
import sys


class Blackjack(object):
    def __init__(self, human=False):
        self.human = human
        self.deck = Deck()
        self.players = []

        # dealer goes to end of list
        self.players.append( self.create_player("Dealer", 1000000) )

        # players get added to the front of list
        self.players.insert( 0, self.create_player("Player_1", 200) )

        self.winner = None
        self.loser = None
        self.pot = []

    def create_player(self, title, cash):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
            cash = raw_input("Enter %s's cash: " % cash)
        else:
            name = title
            cash = 0 if cash == "amount" else cash
        print 'Created Player '+name+' with $'+str(cash)
        return Player(name, cash)


    def play_game(self):

        while len(self.players) > 1: # there are players besides the dealer
            self.play_round()

        return

    def play_round(self):

        # self.bet()
        self.deck.shuffle()
        self.deal()

        # play action goes here

        #self.determine_win_loss()
        #self.do_money()

        self.display_hands()

        self.pause()
        print 'hello'
        sys.exit()

        # card1 = self.draw_card(self.player1, self.player2)
        # card2 = self.draw_card(self.player2, self.player1)
        # self.display_play(card1, card2)
        # if not card1 or not card2:
        #     return
        # if card1 == card2:
        #
        #     self.war()
        #     self.play_round()
        # elif card1 > card2:
        #     self.give_cards(self.player1)
        #     print self.player1, len(self.player1), self.player2 , len(self.player2)
        #
        # else:
        #     self.give_cards(self.player2)
        #     print self.player1, len(self.player1), self.player2 , len(self.player2)


    def deal(self):
        # give each player 1st card, then 2nd card
        for i in range(2):
            for player in self.players:
                player.receive_card( self.deck.draw_card() )

    def display_hands(self):
        for player in self.players:
            player.display_hand()





    def display_play(self, card1, card2):
        if self.human:
            print "%s plays %s" % (self.player1.name, str(card1))
            print "%s plays %s" % (self.player2.name, str(card2))

    def display_receive(self, player):
        if self.human:
            self.pot.sort(reverse=True)
            pot_str = self.cards_to_str(self.pot)
            print "%s receives the cards: %s" % (player.name, pot_str)

    def display_war(self, cards1, cards2):
        if self.human:
            print "WAR!"
            print "%s plays %s" % (self.player1.name, self.cards_to_str(cards1))
            print "%s plays %s" % (self.player2.name, self.cards_to_str(cards2))



    def draw_card(self, player, other_player):
        card = player.play_card()
        if not card:
            self.winner = other_player.name
            self.loser = player.name
            return
        self.pot.append(card)
        return card




    def draw_cards(self, player, other_player, n):
        cards = []
        n = min(n, len(player.hand), len(other_player.hand))
        for i in xrange(n):
            card = self.draw_card(player, other_player)
            if not card:
                return
            cards.append(card)
        return cards

    def war(self):
        cards1 = self.draw_cards(self.player1, self.player2, self.WarCnt)
        cards2 = self.draw_cards(self.player2, self.player1, self.WarCnt)
        self.display_war(cards1, cards2)


    def give_cards(self, player):
        player.receive_cards(self.pot)
        self.display_receive(player)
        self.pot = []

    def pause(self):
        if self.human:
            raw_input("")

    def cards_to_str(self, cards):
        return " ".join(str(card) for card in cards)


    def display_winner(self):
        if self.human:
            print "The winner is %s!!!" % self.winner

    def play_two_of_three(self):
        for i in range(3):
            winner = self.play_game()
            if not self.win_counts.get(winner):
                self.win_counts[winner] = 1
            else:
                self.win_counts[winner] += 1



if __name__ == '__main__':
    game = Blackjack()
    game.play_game()
