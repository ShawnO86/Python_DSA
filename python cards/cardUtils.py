from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#for war
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#for black jack
bj_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #for war
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    
    def __str__(self):
        for card in self.cards:
            print(f'{card.__str__()}')
    
    def shuffle(self):
        shuffle(self.cards)

    def deal_one(self):
        if len(self.cards) == 0:
            raise IndexError('**Deck out of cards**')
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bank = 100

    def add_one(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

    def remove_one(self):
        if len(self.hand) == 0:
            raise IndexError(f'**{self.name}\'s hand out of cards**')
        return self.hand.pop(0)
    
    def make_bet(self, amt):
        if self.bank < amt:
            raise ValueError(f'Not enough in bank! {self.name}\'s balance is {self.bank}.')
        self.bank -= amt
        return f'{self.name} bets {amt}. {self.name}\'s balance is {self.bank}.'
            
    def __str__(self):
        return f'{self.name} has {len(self.hand)} card(s):'