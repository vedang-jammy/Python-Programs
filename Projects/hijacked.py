#this is another cards game I am trying  to build on my own

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10 ,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card:
    def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank
      
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                if suit == 'Dimond' and rank == 'Jack':
                    continue
                else:
                    created_card = Card(suit,rank)
                    self.all_cards.append(created_card)
    
    def Shuffle(self):
        random.shuffle(self.all_cards)        
        