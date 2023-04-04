# Import the following modules and class
from Card import Card
from tkinter import PhotoImage
import random

class DeckOfCards:
    """
    A class used to represent a deck of cards
    
    ...
    
    Attributes
    ----------
    backofcard: card
        Stores the back of card
    deck: list of cards
        Stores the list of card objects
    numcardsdealt: list of cards
        Store the list of card objects that will be dealt
    cardsremaining: int
        Number of card object remaining after dealing (default 52)
    numberlist : int list
        List of card values
    suits : str list
        List of card suits
    
    Methods
    -------
    dealCard()
        Deals and returns card object
    getCardsRemaining()
        Gets/returns the cardsremaining value
    removeCard(card)
        Removes the passed card from the deck
    shuffleDeck()
        Shuffles the deck of card objects
        
    """
    def __init__(self):
        self.__backofcard = Card()
        self.__deck = [0] * 52
        self.__numcardsdealt = []
        self.__cardsremaining = 52
        self.__numberslist = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
        self.__suits = ("C", "S", "D", "H")
        
        # Creates each cards and sets its properties in the deck
        index = 0
        for numindex in range(len(self.__numberslist)):
            for suitindex in range(len(self.__suits)):
                self.__deck[index] = Card()
                self.__deck[index].setImage(PhotoImage(file="images/"+ str(self.__numberslist[numindex])+ self.__suits[suitindex] + ".png"))
                self.__deck[index].setValue(self.__numberslist[numindex])
                # Set the suit
                if self.__suits[suitindex] == "C":
                    self.__deck[index].setSuit("CLUBS")
                elif self.__suits[suitindex] == "H":
                    self.__deck[index].setSuit("HEARTS")
                elif self.__suits[suitindex] == "D":
                    self.__deck[index].setSuit("DIAMONDS")
                else:
                    self.__deck[index].setSuit("SPADES")
                # set the name
                if self.__deck[index].getValue() == 14:
                    self.__deck[index].setName("ACE")
                elif self.__deck[index].getValue() == 13:
                    self.__deck[index].setName("KING")
                elif self.__deck[index].getValue() == 12:
                    self.__deck[index].setName("QUEEN")
                elif self.__deck[index].getValue() == 11:
                    self.__deck[index].setName("JACK")
                else:
                    self.__deck[index].setName(str(self.__deck[index].getValue()))
                index += 1
    
    
    def dealCard(self):
        """
        Deals and returns card object
        Returns
        -------
        card: Card
        """
        self.shuffleDeck()
        card = self.__deck.pop()
        self.__numcardsdealt.append(card)
        self.__cardsremaining -= 1 
        return card

    def getCardsRemaining(self):
        """
        Gets/returns the cardsremaining value
        Returns 
        -------
        ___cardsremaining: int
        """
        return self.__cardsremaining
    
    def removeCard(self, card):
        """
        Removes the passed card from the deck
        Parameters
        ----------
        card: Card
        """
        self.__deck.remove(card)
    
    def shuffleDeck(self):
        """
        Shuffles the deck of card objects
        """
        random.shuffle(self.__deck)
        