import random
from deck import Card

class Player(object):
    def __init__(self, name, wallet, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.status = ''
        self.wallet = wallet
        self.bet_flag = False
        self.bet_amt = 0
        self.busted = False

    def receive_card(self, card):
        self.hand.append(card)

    def if_betting(self):
        return bet_flag

    def set_bet(self, bet_flag):
        self.bet_flag = bet_flag

    def make_bet(self):
        amount = 5
        if (self.wallet > amount):
            self.wallet = self.wallet - amount
            self.bet_amt = amount
            flag = True
        else :
            flag = False
        print self.name+ ' placed bet of $'+str(self.bet_amt)
        return flag

    def play_action(self):
        print self.name+"'s turn...."
        self.display_hand()
        while not self.busted:
            hit = raw_input("Enter Hit Y/N ? : ")
            if hit == 'Y' :
                print "hit"
                self.receive_card(self.deck.draw_card())
                self.display_hand()
                if (self.check_bust()):
                    self.busted = True
                    print 'BUST!!!'
            else:
                print "stay\n"
                break  


    def check_bust(self):
        if self.hand_value() > 21:
            return True
        else:
            return False   

    def hand_value(self):
        card_value = 0
        for card in self.hand:
            card_value += card.get(card)
        return int(card_value)

    def display_hand(self):
        print 'Player '+ self.name + ' hand: '+str(self.hand) + ' = ' + str(self.hand_value())

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand) + len(self.discard)


class Dealer(Player):
    def __init__(self, name, wallet, deck):
        super(Dealer, self).__init__( name, wallet, deck)





