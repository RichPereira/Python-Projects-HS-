from tkinter import PhotoImage

class Bullet:
    """
    A class for the bullet(ship's laser)
    ...
    
    Attributes
    ----------
    canvas: Canvas 
        stores canvas where object will be drawn
    x :int
        x position of bullet
    y:int
        y position of bullet
    imgbullet: PhotoImage 
        image of the bullet 
    width:int
        width of the bullet
    height:int
        height of the bullet
    fired: boolean (default False)
        state of the bullet
    timerid: id (default None)
        timer which keeps track of the shot bullet
    bullet: Bullet
        stores the created/drawn bullet on the canvas
        
    Methods
    -------
    getX()
        returns x coordinate of the bullet
    getY()
        return y coordinate of the bullet
    getWidth()
        returns the width of the bullet
    getHeight()
        returns the height of the bullet
    setX(x)
        sets the x position of the  bullet to the passed x value
    setY(y)
        sets the y position of the  bullet to the passed y value
    setLocation(x, y)
        sets the location of the bullet given the x and y coordinates
    isFired(): Boolean
        returns the state of the bullet as a boolean
    fireBullet()
        fires the bullet by increasing the x coordinate and changes the bullet location accordingly
    deleteBullet()
        deletes the current bullet
    reset()
        cancels the bullet fire timer and sets the is fired to false
    
    """
    def __init__(self, canvas):
        """
        Parameters
        ----------
        canvas: Canvas
            stores canvas where object will be drawn
        """
        self.__canvas = canvas
        self.__x = 0
        self.__y = 0 
        self.__imgbullet = PhotoImage(file = "images/laserbeam.png")
        self.__width = self.__imgbullet.width()
        self.__height = self.__imgbullet.height()
        self.__fired = False
        self.__timerid = None
        self.__bullet = self.__canvas.create_image(self.__x, self.__y, image = self.__imgbullet)

    def getX(self):
        """Returns x coordinate of the bullet
        Returns
        -------
        x:int
            x position of the bullet        
        """
        return self.__x
    
    def setX(self, x):
        """Sets the x position of the  bullet to the passed x value
        Parameters 
        -----------
        x:int
            x position of the bullet       
        """
        self.__x = x
        
    def getY(self):
        """Return y coordinate of the bullet
         Returns
        -------
        y:int
            y position of the bullet       
        """
        return self.__y
     
    def setY(self, y):
        """Sets the y position of the  bullet to the passed y value
        Parameters 
        -----------
        y:int
            y position of the bullet
        """
        self.__y = y 
    
    def getWidth(self):
        """Returns the width of the bullet
        Returns
        -------
        width:int
            width of the current bullet
        """
        return self.__width
    
    def getHeight(self):
        """Returns the height of the bullet
        Returns
        -------
        height:int
            height of the bullet
        """
        return self.__height
    
    def setLocation(self, x, y):
        """Sets the location of the bullet given the x and y coordinates
        Parameters
        ----------
        x:int
            x position of the bullet
        y:int
            y position of the bullet  
        """
        self.__x = x
        self.__y = y
        self.__canvas.coords(self.__bullet, self.__x, self.__y)
        
    def isFired(self):
        """Returns the state of the bullet as a boolean
        Returns
        -------
        fired: boolean
            current state of the bullet
        """
        return self.__fired
    
    def fireBullet(self):
        """Fires the bullet by increasing the x coordinate, changing the state to true and the bullet location accordingly
        """
        self.__fired = True
        self.__x += 5
        self.__canvas.coords(self.__bullet, self.__x, self.__y)
        self.__timerid = self.__canvas.after(3, self.fireBullet)
        
    def deleteBullet(self):
        """Deletes the current bullet
        """
        self.__canvas.delete(self.__bullet)
    
    def reset(self):
        """Cancels the bullet fire timer and sets the is fired to false
        """
        try:
            self.__timerid = self.__canvas.after_cancel(self.__timerid)
            self.__fired = False
        except ValueError:
            pass
        
