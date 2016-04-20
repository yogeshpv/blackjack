from blackjack_deck import Deck
from blackjack_player import Player, Dealer
import sys


class Blackjack(object):
    def __init__(self, human=False):
        self.human = human
        self.deck = Deck()
        self.players = []

        # dealer goes to end of list
        self.players.append( self.create_dealer("Dealer", 1000000, self.deck) )

        # players get added to the front of list
        self.players.insert( 0, self.create_player("Player_1", 200, self.deck) )

        self.winner = None
        self.loser = None
        self.pot = []

    def create_dealer(self, title, cash, deck):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
            cash = raw_input("Enter %s's cash: " % cash)
        else:
            name = title
            cash = 0 if cash == "amount" else cash
        print 'Created Dealer '+name+' with $'+str(cash)
        return Dealer(name, cash, deck)


    def create_player(self, title, cash, deck):
        if self.human:
            name = raw_input("Enter %s's name: " % title)
            cash = raw_input("Enter %s's cash: " % cash)
        else:
            name = title
            cash = 0 if cash == "amount" else cash
        print 'Created Player '+name+' with $'+str(cash)
        return Player(name, cash, deck)



    def play_game(self):
        print '=== start playin ==='
        # while len(self.players) > 1: # there are players besides the dealer
        self.play_round()

        self.pause()
        print '=== play 1 round & exit ==='
        sys.exit()

        return

    def play_round(self):

        self.place_bets()
        self.deck.shuffle()
        self.deal()

        self.display_hands()

        # play action
        print '\n--- play action! ---'
        for player in self.players:
            player.play_action()

        self.determine_win_loss()
        self.do_money()

        self.display_hands()

    def place_bets(self):
        print '\n--- placing bets ---'
        for player in self.players:
            player.make_bet() # returns a false if out of $$$. need to do something.....
        return

    def deal(self):
        print '\n--- dealing hands ---'
        # give each player 1st card, then 2nd card
        for i in range(2):
            for player in self.players:
                player.receive_card( self.deck.draw_card() )

    def determine_win_loss(self):
        print '\n--- deterining winners / losers ---'

        # check dealer status...
        dealer = self.players[-1]
        if dealer.busted:
            print 'Dealer BUSTED. EVERYONE WIN!!!!!!!'
        else:
            dealer_value = dealer.hand_value()
            print 'Dealer = '+str(dealer_value)

            # loop thru each player
            for player in self.players[:-1]:
                player_val = player.hand_value()
                print player.name+' hand = '+str(player_val)
                if player_val > dealer_value and (not player.busted):
                    print player.name+' WON!'
                else:
                    print player.name+' Loss...'


    def do_money(self):
        print '\n--- do money ---'
        for player in self.players:
            pass
        pass

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
