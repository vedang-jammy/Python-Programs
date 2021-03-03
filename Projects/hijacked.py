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
        return self.rank  + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                if suit == 'Diamonds' and rank == 'Jack':
                    break
                else:
                    self.all_cards.append(Card(suit,rank))
   
   #test function
    def __str__(self):
        deck_comp = ' ' #start with emty string
        for card in self.all_cards:
            deck_comp += '\n '+card.__str__() #add each card object print string
        return 'The deck has:' + deck_comp
    
    def Shuffle(self):
        random.shuffle(self.all_cards)        
       
    #for dealing random cards to players
    def deal_one(self):
        new_card = self.all_cards.pop(0)
        return new_card
    
class Player:
    def __init__(self,name):
        self.name = name
        self.player_cards = [] #empty list for storing players cards
    
    def add_cards(self,new_card):
        self.player_cards.append(new_card)
            
    def remove_pairs(self):
        for suit,rank in self.player_cards:
            for i in range(0,len(self.player_cards)+1):
                if self.player_cards[i] == self.player_cards[i+1]:
                    self.player_cards.pop(i,i+1)

    def __str__(self):
        deck_comp = ' ' #start with emty string
        for card in self.player_cards:
            deck_comp += '\n '+card.__str__() #add each card object print string
        return 'The player has:' + deck_comp
    
                    
test_deck = Deck()
test_deck.Shuffle()

player1 =  Player('One')
player2 = Player('Two')

for i in range(0,51):   
    player1.add_cards(test_deck.deal_one())
    player2.add_cards(test_deck.deal_one())
    
print(player1)

print(player2)
# player1.remove_pairs()
# player2.remove_pairs()



