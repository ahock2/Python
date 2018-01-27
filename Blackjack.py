# File: Blackjack.py

"""
Name: Blackjack.py

Creator: Adam Hock

Date started: 1/17/2018

Description:    This program is a single player Blackjack game where
                you play against a dealer.

Comments:       I have a few ideas for changes to this program in the future
                concerning topics such as a point system, A.I., and multiplayer
                features.
                
                
"""

import random, time

def Wait():
        """
        This function makes the program wait two seconds when it is called
        I made it a function so I can easily change all wait times simultaneously
        """
        time.sleep(2)

def DrawCard(score, card):
        """
        This function adds the drawn card to the player's score
        """
        if card == 'jack' or card == 'queen' or card == 'king':
                score+=10
        elif card == 'ace':
                score+=1
        else:
                score+=card
        return score

def Comparison(you, dealer):
        """
        This function compares the score of the player to the dealer
        """
        Wait()
        if you == 0 and dealer == 0:
                print("\nYou guys both busted, so it was a DRAW!\n")
        elif you == dealer:
                print("\nYou guys both got the same score, so it was a DRAW!\n")
        elif you < dealer:
                print("\nThe dealer has a higher score than you, so you LOSE!\n")
        elif you != 0 and dealer == 0:
                print("\nThe dealer busted! you WIN!\n")
        else:
                print("\nYour score is better than the dealer's, so you WIN!\n")
        input("Press Enter to continue...")

def PlayHand(score, aces, cards = [], *args):
        """
        This function plays the turn of the player
        """
# This loop will execute until the player busts or stays
        while True:
                choice = str(input("\nWould you like to \'hit\' or \'stay\'?\n"))
                if choice == "hit":
                        z = cards[0]
                        cards.remove(z)
                        print("\nYou have been dealt the following card:\n")
                        print(z)
                        if z == 'ace':
                                aces = True
                                score+=1
                        else:
                                score = DrawCard(score, z)
                        if score > 21:
                                print("\nYou Busted!\n")
                                return 0
                        else:
                                continue
                elif choice == "stay":
                        if score < 12 and aces == True:
                                score+=10
                        else:
                                score+=0
                        print("\nThis is your score!\n")
                        print(score)
                        return score
                else:
                        print("\nInput Error! Try again\n")
                        continue

# The following loop will execute until the user exits the game
                
while True:
        cards = [
        2, 2, 2, 2, 
        3, 3, 3, 3, 
        4, 4, 4, 4, 
        5, 5, 5, 5, 
        6, 6, 6, 6, 
        7, 7, 7, 7,
        8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10, 10,
        'jack', 'jack', 'jack', 'jack',
        'queen', 'queen', 'queen', 'queen',
        'king', 'king', 'king', 'king',
        'ace', 'ace', 'ace', 'ace',
        ]

        random.shuffle(cards)

        player1 = 0
        player1_Aces = False

        dealer = 0

        print("Welcome to BlackJack! For future reference, THE DEALER WILL HIT UNTIL HE REACHES 17 OR HIGHER.\n")
        print("Also, the dealer still hits on a \'soft\' 17, which simply means HE ONLY COUNTS ACES AS 1 (NOT 11).\n")
        print("The dealer deals you and himself each two cards...\n")

#The following lines deal cards. It sets a variable as the top card on the deck
#And then that card's value is removed from the deck
        
        x = cards[0]
        cards.remove(x)
        dealerX = cards[0]
        cards.remove(dealerX)
        y = cards[0]
        cards.remove(y)
        dealerY = cards[0]
        cards.remove(dealerY)

        print("These are the two cards you have been dealt\n")
        print(x)
        print(y)
        input("\nPress Enter to continue...")

        print("\nThis is the value of the dealer's face-up card\n")
        print(dealerY)
        input("\nPress Enter to continue...")

        if x == 'ace':
                player1_Aces = True
        else:
                player1 = player1
        player1 = DrawCard(player1, x)

        split1 = player1
        
        if y == 'ace':
                player1_Aces = True
        else:
                player1 = player1 = player1
        player1 = DrawCard(player1, y)

        dealer = DrawCard(dealer, dealerX)
        dealer = DrawCard(dealer, dealerY)
                
#The following loop will execute until the user's turn is done
        while True:
                if x==y:
                        split = str(input("\nWould you like to split? Type \'yes\' or \'no\'\n"))
                        if split == "yes":
                                split2 = split1
                                print("\nThis is the value of your first hand\n")
                                print(split1)
                                split1 = PlayHand(split1, player1_Aces, cards)
                                input("\nPress Enter to continue...")
                                
                                print("\nThis is the value of your second hand\n")
                                print(split2)
                                split2 = PlayHand(split2, player1_Aces, cards)
                                input("\nPress Enter to continue...")
                                print("\nThis is your final score after both hands!\n")
                                if split1 == 0 and split2 == 0:
                                        print("\nBoth of your hands busted!\n")
                                        break
                                elif split1 > split2:
                                        print(split1)
                                        player1 = split1
                                        break
                                else:
                                        print(split2)
                                        player1 = split2
                                        break
                        elif split == "no":
                                player1 = PlayHand(player1, player1_Aces, cards)
                                break
                        else:
                                print("\nInvalid Input!\n")
                                continue
                else:
                        player1 = PlayHand(player1, player1_Aces, cards)
                        break
        input("\nPress Enter to continue...")
        print("\nNow it's time for the dealer's turn to play. Remember, this was his first card\n")
        print(dealerY)
        input("\nPress Enter to continue...")
        print("\nThe dealer flips his other card...\n")
        Wait()
        print(dealerX)

#The following loop will execute until the dealer's turn is done
        if (dealerX == 'ace' or dealerY == 'ace') and dealer == 11:
                Wait()
                print("\nThe dealer has blackjack!\n")
                Comparison(player1, 21)
        else:
                while True:
                        if dealer > 21:
                                Comparison(player1, 0)
                                break
                        elif dealer > 16:
                                Wait()
                                print("\nThe dealer stays...\n")
                                Wait()
                                print("\nThis is the dealer's final score\n")
                                print(dealer)
                                Comparison(player1, dealer)
                                break
                        else:
                                Wait()
                                print("\nThe dealer hits...\n")
                                dealerZ = cards[0]
                                cards.remove(dealerZ)
                                Wait()
                                print("\nThe dealer drew the following card\n")
                                print(dealerZ)
                                dealer = DrawCard(dealer, dealerZ)
                                continue
        while True:        
                print("\nWould you like to play again?\n")
                again = str(input("\nType \'yes\' or \'no\'\n"))
                if again != "yes" and again != "no":
                        print("\nInvalid input!\n")
                        continue
                else:
                        break

        if again == "yes" :
                for i in range(50):
                        print()
        else:
                break
