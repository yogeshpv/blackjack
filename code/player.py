import random
from deck import Card

class Player(object):
    def __init__(self, name, wallet):
        self.name = name
        self.hand = []
        self.status = ''
        self.wallet = wallet
        self.bet_flag = False

    def receive_card(self, card):
        self.hand.append(card)

    def if_betting(self):
        return bet_flag

    def set_bet(self, bet_flag):
        self.bet_flag = bet_flag

    def make_bet(self, amount):
        if (self.wallet > amount):
            self.wallet = self.wallet - amount
            return True
        else :
            return False

    def play_action(self):
        pass

    def hand_value(self):
        card_value = 0
        for card in self.hand:
            card_value += card.get(card)
        return card_value

    def display_hand(self):
        print 'Player '+ self.name + ' hand: '+str(self.hand)
        print self.hand_value()

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand) + len(self.discard)


class Dealer(Player):
    def __init__(self, name, wallet = 1000):
        super(Dealer, self).__init__( name, wallet)





