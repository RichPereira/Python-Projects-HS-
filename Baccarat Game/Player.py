#Import the following class
from Card import Card

class Player:
    """
    A class used to represent a player
    ...
    
    Attributes
    ----------
    playerCardsList: card list
        Stores the 3 cards
    deck: list of cards
        Stores the list of card objects
    score: int
        stores the sum of the all the cards(default 0)
        
    Methods
    -------
    getCards(index)
        Returns the card object at the passed index of the playerCardslist
    
    dealCards(num)
        Deals a card to the stored cards at the num index of the playerCardslist
    
    playerScore() 
        Adds the values of the cards to the score and returns the score
    """
    
    def __init__(self, deck):
        self.__playerCardsList = [Card(), Card(), Card()]
        self.__deck = deck
        self.score = 0
 
    def getCards(self, index):
        """
        Returns the card object at the passed index of the playerCardslist
        Parameters
        ----------
        index: int
        
        Returns
        -------
        ___playerCardsList[index]: Card
        """
        return self.__playerCardsList[index]
 
    def dealCards(self, num):
        """
        Deals a card to the stored cards at the num index of the playerCardslist
        
        Parameters
        ----------
        num: int
        """
        self.__playerCardsList[num] = self.__deck.dealCard()
 
    def playerScore(self):
        """
        Adds the values of all the cards at the following index
        If sum is greater than 9, only uses the units place of the sum value
        
        Returns
        -------
        score: int
        """
        self.score = self.__playerCardsList[0].addCard() + self.__playerCardsList[1].addCard() + self.__playerCardsList[2].addCard()
        if self.score > 9:
            self.score = (self.score % 10)
        return self.score
    