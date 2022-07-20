from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    def __init__(self):
        print("Creating a deck of cards")
        self.cards=[(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        shuffle(self.cards)
    def split_into_two(self):
        return (self.cards[:26],self.cards[26:])
class Hand:
    def __init__(self,cards):
        self.cards=cards
    def add_card(self,cards_won):
        self.cards.extend(cards_won)
    def remove_card(self):
        return self.cards.pop()
class Player(Hand):
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        return self.hand.remove_card()
    def play_war_card(self):
        war_cards=[]
        if len(self.hand.cards)>3:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards
        else:
            return False
    def still_has_cards(self,check4=False):
        if (check4):
            return len(self.hand.cards)>3
        else:
            return len(self.hand.cards)!=0
d=Deck()
d.shuffle()
h1,h2=d.split_into_two()
print(f"Computer: {h1}")
print(f"User: {h2}")
computer=Player("Computer",Hand(h1))
user=Player("User",Hand(h2))
war_count=0
war_cards=[]
counter=0
while user.still_has_cards() and computer.still_has_cards():
    counter+=1
    comp_card=computer.play_card()
    user_card=user.play_card()
    cards_in_action=[]
    cards_in_action.append(user_card)
    cards_in_action.append(comp_card)
    if user_card[1]==comp_card[1]:
        war_count+=1
        print("There is war")
        if (computer.still_has_cards(check4=True)):
            cards_in_action.extend(computer.play_war_card())
        else:
            print("User won")
            break
        if (user.still_has_cards(check4=True)):
            cards_in_action.extend(user.play_war_card())
        else:
            print("Computer won")
            break
        if(user.hand.cards[-1][1]==computer.hand.cards[-1][1]):
            war_cards.extend(cards_in_action)
        else:
            comp_card=computer.play_card()
            user_card=user.play_card()
            cards_in_action.append(comp_card)
            cards_in_action.append(user_card)
            if RANKS.index(user_card[1])>RANKS.index(comp_card[1]):
                user.hand.add_card(cards_in_action)
                if not (computer.still_has_cards()):
                    print("User won")
                    break
            else:
                computer.hand.add_card(cards_in_action) 
                if not (user.still_has_cards()):
                    print("Computer won")
                    break
    else:
        war_cards=[]
        if RANKS.index(user_card[1])>RANKS.index(comp_card[1]):
            user.hand.add_card(cards_in_action)
        else:
            computer.hand.add_card(cards_in_action) 
        if not user.still_has_cards():
            print("Computer won")
            break
        elif not computer.still_has_cards():
            print("User won")
            break
