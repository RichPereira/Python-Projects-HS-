from tkinter import PhotoImage

class Card:
    """
    A class used a card object
    ...
    
    Attributes
    ----------
    value : int
        Value of the card object
    suit: str
        Suit of the card object
    name: str
        Name of the card object
    imgCard: PhotoImage
        Image of the card object(default back card)        
    width : int 
        Width of the imgCard        
    height: int
        Height of the imgCard   
    sum : int
        Sum of the card values(default 0)       
    
    Methods
    -------
    getImage()
        Gets the current image of the card   
    setImage(image)
        Sets the image to the passed image   
    getName()
        Gets the current name as string   
    setName(cardname)
        Sets the name to the passed name    
    getValue()
        Gets the current value of the card object  
    setValue(cardval)
        Sets the value of the card to the passed value   
    setSuit(cardsuit)
        Sets the suit of the current card to the passed suit 
    getSuit()
        Gets the suit of the current card object
    addCard()
        Returns the changed value of the score
    """
    
    def __init__(self):
        self.__value = 0
        self.__suit = ""
        self.__name = str(self.__value) + " of " + self.__suit
        self.__imgCard = PhotoImage(file="images/back_blue.png")
        self.__width = self.__imgCard.width()
        self.__height = self.__imgCard.height()
        self.sum = 0
        
    def getImage(self):
        """
        Gets the current image of the card 
        Returns 
        ------- 
        __imgCard: PhotoImage
        
        """
        return self.__imgCard
    
    def getName(self):
        """
        Gets the current name as string
        Returns 
        ------
        __name: str
        """
        return self.__name
    
    def getValue(self):
        """
        Gets the current value of the card object  
        Returns
        -------
        __value: int
        """
        return self.__value
    
    def getSuit(self):
        """
        Gets the suit of the current card object
        Returns
        -------
        __suit: str
        """
        return self.__suit
    
    def setImage(self, img):
        """
        Sets the image to the passed image 
        Parameters
        ----------
        img: PhotoImage
        """
        self.__imgCard = img
        
    def setName(self, cardname):
        """
        Sets the name to the passed name 
        Parameters
        ----------
        cardname : str
        """
        self.__name = cardname
        
    def setValue(self, cardval):
        """
        Sets the value of the card to the passed value 
        Parameters
        ----------
        cardval: int
        """
        self.__value = cardval
        
    def setSuit(self, cardsuit):
        """
        Sets the suit of the current card to the passed suit
        Parameters
        ----------
        cardsuit: str
        """
        self.__suit = cardsuit
        
    def addCard(self):
        """
         Sets the value of the cards Ace, king, queen, jack , 10 to 1 or 0  and add the value to variable
         Returns
         -------
         __sum: int
        """
        self.sum = 0
        if self.__name == "ACE":
            self.__value = 1
        elif self.__name == "KING" or self.__value == 13 or self.__name == "QUEEN" or self.__value == 12 or self.__name == "Jack" or self.__value == 11:
            self.__value = 0
        else:
            self.__value = self.__value
        self.sum += self.__value
        return self.sum