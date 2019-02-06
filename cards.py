def __eq__(self,other):
    return self.rank==other.rank and self.suit==other.suit

class Decks:
   def __init__(self):
     self.cards=[]
     for suit in range(4):
      for rank in range(1,14):
        card=card(suit,rank)
        self.cards.appennd(card)
ace_of_spade=card(1,3)
print(ace_of_spade)
