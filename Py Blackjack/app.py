import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two', 
    'Three', 
    'Four', 
    'Five', 
    'Six', 
    'Seven', 
    'Eight', 
    'Nine', 
    'Ten', 
    'Jack', 
    'Queen',
    'King', 
    'Ace'
)
values = { 
    'Two':2, 
    'Three':3, 
    'Four':4, 
    'Five':5, 
    'Six':6, 
    'Seven':7, 
    'Eight':8, 
    'Nine':9, 
    'Ten':10, 
    'Jack': 10, 
    'Queen':10, 
    'King': 10, 
    'Ace':11
}

playing = True

# CLASS DEFINITIONS
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        complete_deck = ''
        for card in self.deck:
            complete_deck += '\n' + card.__str__()
        return 'The deck has: ' + complete_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total=100): 
        self.total = total #100 is set as the default total if none is provided by user
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# END OF CLASS DEFINITIONS

# FUNCTION DEFINITIONS

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter the bet you want to wage: "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("That's too high of a bet. Your bet can't exceed " + str(chips.total))
            else:
                print("Bet placed.")
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        decision = input("Hit or Stand?\n")

        if decision[0].lower() == 'h':
            hit(deck,hand)
        elif decision[0].lower() == 's':
            print("Player stands. Dealer is playing")
            playing = False
        else:
            print("Please enter hit or stand to proceed")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print("<card hidden> | " + str(dealer.cards[1]))
    print("\nPlayer's Hand:\n", *player.cards, sep=" | ")

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep=" | ")
    print("Dealer's Hand = ", dealer.value)
    print("Player's Hand: ", *player.cards, sep=" | ")
    print("PLayer's Hand = ", player.value)

def player_bust(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_bust(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# END OF FUNCTION DEFINITIONS


# START OF GAME LOOP
while True:
    #print opening statement
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.")

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()
    
    # Creat and deal two cards to dealer and player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips() #default is 100

    # Prompt the Player fpr their bet
    take_bet(player_chips)

    # Show start cards
    show_some(player_hand, dealer_hand)

    while playing: 

        # Prompt for Player Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards, keeping one dealer card hidden
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted and chose to stand, dealer plays until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand,dealer_hand)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break    

# END OF GAME LOOP