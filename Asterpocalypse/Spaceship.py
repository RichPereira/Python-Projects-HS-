from tkinter import PhotoImage

class Spaceship:
    """
    A class for the spaceship in space
    ...
    
    Attributes
    ----------
    canvas: Canvas 
        stores canvas where object will be drawn
    x : int
        x position of ship
    y: int
        y position of ship
    imgship: PhotoImage
        stores image of the spaceship
    imgblast: PhotoImage
        stores image of the exploded spaceship
    spaceship: Spaceship
        stores the drawn ship object
    
    Methods
    -------
    setLocation(x,y)
        sets the location of the ship given the x and y coordinates
    getX()
        returns x coordinate of the ship
    getY()
        return y coordinate of the ship
    getWidth()
        returns the width of the ship
    getHeight()
        returns the height of the ship
    setX(x)
        sets the x position of the ship to the passed x value
    setY(y)
        sets the y position of the ship to the passed y value 
    explode()
        sets the image of the ship to the exploded ship
    
    """
    def __init__ (self, canvas, x, y):
        """
        Parameters
        ----------
        canvas: Canvas
            stores canvas where object will be drawn
        x : int
            stores x position of the ship
        y: int
            stores y position of the ship
        """
        self.__canvas = canvas
        self.__x = x 
        self.__y = y
        self.__imgship = PhotoImage(file = "images/spaceship.png")
        self.__imgblast = PhotoImage(file = "images/exploded_ship.png")
        self.__spaceship = self.__canvas.create_image(self.__x, self.__y, image = self.__imgship)
        
    def setLocation(self, x, y):
        """Sets the location of the ship given the x and y coordinates
        
        Parameters
        ----------
        x: int
            x position of the ship
        y: int
            y position of the ship
        """
        self.__x = x
        self.__y = y 
        self.__canvas.itemconfig(self.__spaceship, image = self.__imgship, anchor = "nw")
        self.__canvas.coords(self.__spaceship, self.__x, self.__y)
    
    def getWidth(self):
        """Returns the width of the ship
        Returns
        -------
        width:int
            width of the ship
        """
        return self.__imgship.width()
    
    def getHeight(self):
        """Returns the height of the ship
        
        Returns
        -------
        height:int
            height of the ship
        """
        return self.__imgship.height()
    
    def getX(self):
        """Returns x coordinate of the ship
        
        Returns
        -------
        x:int
            x position of the ship
        """
        return self.__x
    
    def setX(self, x):
        """Sets the x position of the ship to the passed x value
        
        Parameters
        ----------
        x: int
            x position of the ship
        """
        self.__x = x
    
    def getY(self):
        """Return y coordinate of the ship
        
        Returns
        -------
        y:int
            y position of the ship
        """
        return self.__y
    
    def setY(self, y):
        """Sets the y position of the ship to the passed y value 
        
        Parameters
        ----------
        y: int
            y position of the ship
        
        """
        self.__y = y
    
    def explode(self):
        """Sets the image of the ship to the exploded ship
        """
        self.__canvas.itemconfig(self.__spaceship, image = self.__imgblast)

        