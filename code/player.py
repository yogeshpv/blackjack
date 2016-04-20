import random

class Player(object):
    def __init__(self, name, wallet):
        self.name = name
        self.hand = []
        self.discard = []
        self.status = ''
        self.wallet = wallet
        self.bet_flag = False

    def receive_card(self, card):
        self.discard.append(card)

    def receive_cards(self, cards):
        self.discard.extend(cards)

    def play_card(self):
        if not self.hand:
            random.shuffle(self.discard)
            self.hand = self.discard
            self.discard = []
        if not self.hand:
            return None
        card = self.hand.pop()
        return card

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
        self.hand

    def display_hand(self):
        print 'Player '+self.name+' hand: '+str(self.hand)

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand) + len(self.discard)