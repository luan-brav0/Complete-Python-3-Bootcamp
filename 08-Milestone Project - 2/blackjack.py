'''Blackjack game made by Luan de Melo Bravo (@luan_brav0) as a practice of fundamentals of OOP. Course by Pierian Data
This is a slight adaptation of mine based the walkthrough activity in this folder so that it could be futuraly scalable to a multiplayer blackjack vitual table.'''
import random

# -- CARDS --
# Card values: 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    
    def __init__(self,suit,rank):
        '''Assumes strings stuit and rank
        Card has suit, rank and a value relative to the value dict.'''
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        # i.e.: 'Two of hearts'
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        '''Deck class has a list deck'''
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        '''Returnts a list of the cards in deck as strings.'''
        str_deck = []
        for card in range(len(self.deck)):
            str_deck.append(str(self.deck[card]))
        return str(str_deck)

    def shuffle(self):
        '''Returns None
        Shuffles cards in deck'''
        print("\nShuffling the deck...")
        random.shuffle(self.deck)
        
    def deal(self):
        '''Returns a type Card
        Takes (pops) a card from the deck  to be dealt.'''
        print("\nDealing cards...")
        return self.deck.pop()

class Hand:
    def __init__(self, name):
        '''Assumes string name for player's name.
        Hand has list cards, int value, and bool aces.'''
        self.name = name
        self.cards = []
        self.value = 0   # total value of cards in hand
        self.aces = True if 'Ace' in self.cards else False # if there is an Ace in hand
    
    def __str__(self):
        '''Retuns list of strings of cards in self.cards
        Takes cards type Card in list self.cards, gets string of each Card and appends to returned list.'''
        str_cards = []
        for card in range(len(self.cards)):
            str_cards.append(str(self.cards[card]))
        return str(str_cards)

    
    def adjust_for_ace(self):
        '''Returns int self.value
        Checks if there are aces in hand and adjusts value as necessary.'''
        self.aces = True if 'Ace' in self.cards else False
        if self.aces and self.value < 21:
            pass
        elif self.aces and self.value > 21:
            self.value -= 10
        return self.value
    
    def add_card(self,card):
        '''Assumes Card type. 
        Returns None.
        Appends card to hand and updates self.value relative to dict values.
        *Already applies adjust for aces function!*'''
        self.cards.append(card)
        self.value += values.get(str(card).split()[0])
        self.value = self.adjust_for_ace()
    
    def hit(self, deck):
        '''Assumes and returs lists deck and hand.
        Takes the last card of the deck, adds to the given hand and checks for results'''
        self.add_card(deck.deal())



class Chips:
    
    def __init__(self):
        self.total = 0
        while True:
            try:
                self.total = int(input("\nHow much would you like to buy in casino chips? : ")) if self.total == 0 else self.total
                if self.total <= 0:
                    raise ValueError
                else: 
                    break
            except ValueError:
                print("Please enter a valid ammont in chips")
        self.bet = 0

    def win_bet(self):
        self.total += self.bet * 2  
        self.bet = 0

    def lose_bet(self):
        self.bet = 0
    
    # def double_bet(self):

    def take_bet(self):
        '''Returns int bet
        Asks user to input desired value to be bet within his current ammount of chips.'''
        while self.bet <= 0 :
            try:
                self.bet = int(input(f"\nTotal : USD${self.total}\nEntry betting ammount : USD$"))
            except ValueError:
                print("Please enter a valid betting amount.")
            finally:
                if self.bet > self.total or self.bet < 0:
                    raise ValueError("\nPlease enter a valid betting amount.")
                self.total -= self.bet
                    
        return self.bet



def check_hand(hand):
    '''Assumes int hand.
    Returns string
    Checks the difference of 21 and hand value.'''
    hand = hand
    if hand.value == 21 and len(hand.cards) == 2:
        # print("BLACKJACK")
        return "BLACKJACK"
    elif hand.value <= 21:
        # print("WINS")
        return "WINS"
    elif hand.value > 21:
        # print("BUST")
        return "BUST"

def check_push(player,dealer):
    '''Assumes Hands player and dealer
    Returns String | None
    Checks, if not bust, if a push happened.'''
    if check_hand(player) != "BUST" and check_hand(dealer) != "BUST":
        if player == dealer:
            return "PUSH"



def hit_or_stand(deck, hand):
    '''Assumes Hand hand
    Returns bool playing
    Prompts the user to select if they would like to hit (draw a card) or stand (keep cards).'''
    global playing  # to ansrol an upcoming while loop
    hit_or_stand = ''
    while playing:
            
            hit_or_stand = input("\nWould you like to [H]it or [S]tand? [H/S] : ").upper()
            if hit_or_stand not in ('H', 'S'):
                raise ValueError("\nPlease enter a valid input : ['H'/'S']")
            if hit_or_stand == 'H':
                hand.hit(deck)
                playing = True if check_hand(hand) != "BUST" or check_hand(hand) != "BLACKJACK" else False
                return playing
            else:
                playing = False
                return playing
    return playing
                 


def show_some(player,dealer):
    '''Assumes classes player and dealer.
    Returns None
    Prints one of the dealer's cards and all the player's cards.'''
    print(f"\nDealer's Hand : {str(dealer.cards[0])} ({values.get(str(dealer.cards[0]).split()[0])})")
    print(f"Player's Hand : {str(player)} ({player.value})")

def show_all(player,dealer):
    '''Assumes classes player and dealer.
    Returns None
    Prints all the cards and values of each hand.'''
    print(f"\nDealer's Hand : {dealer} ({dealer.value})")
    print(f"Player's Hand : {player} ({player.value})") 

def play_again(player, dealer):
        ans = ""
        while ans not in ["Y", "N"]:
            ans = input("\nPlay again? [Y/N] : ").upper()
        if ans == "Y":
            player.cards = []
            player.value = 0
            dealer.cards = []
            dealer.value = 0
            return True
        else:
            return False

def play(deck, chips, player,dealer):
    global playing
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    show_some(player, dealer)
    # If player's hand exceeds 21, run player_busts() and break out of loop
    while player.value < 21 and playing == True:
        # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        # Show cards (but keep one dealer card hidden)
        playing = hit_or_stand(deck, player) # returns playing == True if 
        show_some(player, dealer)
        check_hand(player)
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if check_push(player,dealer) == "PUSH":
            print("\nPUSH!")
    if check_hand(player) == "BUST":
        chips.lose_bet()
        print("\nPLAYER BUST!")
        print("\nPlayer lost!")
    elif check_hand(player) == "BLACKJACK" and check_push(player,dealer) != "PUSH":
        chips.win_bet()
        print("\nPLAYER BLACKJACK!" * 5)
        print("\nPlayer wins!")
    # Run different winning scenarios
    elif check_hand(player) == "WINS":
        while (dealer.value < player.value or dealer.value <= 17) and check_hand(dealer) == "WINS":
            print("\nDealer hits...")
            dealer.hit(deck)
        
        if check_hand(dealer) == "WINS":
            chips.lose_bet()
            print("\nDEALER WINS!")
            print("\nPlayer lost!")
        elif check_hand(dealer) == "BUST":
            chips.win_bet()
            print("\nDEALER BUST!")
            print("\nPlayer wins!")
            playing = False
        
        elif check_hand(dealer) == "BLACKJACK":
            chips.lose_bet()
            print("\nDEALER BLACKJACK!"*5)
            print("\nPlayer lost!")
            playing = False
        else:
            chips.win_bet()
            print("\nDEALER LOST!")
            print("\nPlayer wins!")
            playing = False
    # Show all cards
    show_all(player,dealer)
    return chips.total

def main():
    '''BLACKJACK GAME!'''
    while True:
        # Print an opening statement
        print("\nWELCOME TO THE GAME OF BLACKJACK!")

        # Create & shuffle the deck, deal two cards to each player


        # Set up the Player's chips
        chips = Chips ()
        # Prompt the Player for their bet

        chips.take_bet()

        # Show cards (but keep one dealer card hidden)
        deck = Deck()
        deck.shuffle()

        player = Hand("Player")
        dealer = Hand("Dealer")

        

        # Play runs the game and returns the total value that player has in chips
        chips.total = play(deck,chips,player, dealer)
        
        # Inform Player of their chips total 
        print(f"\nTotal Chips : {chips.total}\n")

        # Ask to play again
        game_on = play_again(player, dealer)
        while game_on == True and chips.total > 0:
            chips.total = play(deck, chips, player, dealer)
            game_on = play_again(player, dealer)
        # break
        else:
            # Inform Player of their chips total 
            print(f"\nTotal Chips : {chips.total}")
            break

if __name__ == "__main__":
    main()