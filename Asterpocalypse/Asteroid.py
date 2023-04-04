from tkinter import PhotoImage
import random

class Asteroid:
    """
    A class that represents an asteroid in space
    ...
    
    Attributes
    ----------
    canvas: canvas
        stores the imported canvas
    imgAsteroids: PhotoImage
        creates and stores asteroid images
    imgBlast: PhotoImage
        creates and stores asteroid blasts
    x:int
        x position of asteroid (default 1060)
    y:int
        y position of asteroid
    value:int
        value of the asteroid
    speed:int
        stores speed of the asteroid(default 50)
    currentAsteroid: PhotoImage
        stores the current image of the asteroid
    asteroid: Asteroid
        stores the created asteroid object 
 
    Methods
    -------
    getX()
        returns x coordinate of the asteroid
    getY()
        return y coordinate of the asteroid
    getWidth()
        returns the width of the current asteroid
    getHeight()
        return the height of the current asteroid 
    move()
        moves the asteroid certain spaces at a certain speed and sets its coordinates accordingly 
    showBlast()
        cancels the movement of the asteroid and shows the blast image and then deletes the asteroid
    delete()
        deletes the current asteroid
    stopMovement()
        stops the movement of the asteroid
    
    """
    def __init__(self, canvas, speed = 15):
        """
        Parameters
        ----------
        canvas: Canvas 
            the canvas where the asteroid user wants to draw on
        speed:int
            the speed of the asteroid
        
        """
        self.__canvas = canvas
        self.__imgAsteroids =["", PhotoImage(file ="images/asteroid0.png"), PhotoImage(file ="images/asteroid1.png"), PhotoImage(file ="images/asteroid2.png")]
        self.__imgblast = ["", PhotoImage(file = "images/explosion0.png"), PhotoImage(file = "images/explosion1.png"), PhotoImage(file = "images/explosion2.png")]
        self.__x = 1160
        self.__y = random.randint(52, 407)
        self.__value = random.randint(1, 3)
        self.__speed = speed
        self.__currentAsteroid = self.__imgAsteroids[self.__value]
        self.__asteroid = self.__canvas.create_image(self.__x, self.__y, image = self.__currentAsteroid, anchor = "ne")
        self.__mId = None
        self.move()
    
    def getX(self):
        """ Returns x coordinate of the asteroid
        Returns
        -------
        x-position:int
            returns x coordinate of the current asteroid
        """
        return self.__x
    
    def getY(self):
        """Return y coordinate of the asteroid
        Returns
        -------
        y-position:int
            y-coordinate of the asteroid
        """
        return self.__y
    
    def getWidth(self):
        """Returns the width of the current asteroid
        Returns
        -------
        width:int 
            width of the asteroid        
        """
        return self.__currentAsteroid.width()
    
    def getHeight(self):
        """Return the height of the current asteroid 
        Returns
        -------
        height
            returns height of the asteroid
        """
        return self.__currentAsteroid.height()

    def move(self):
        """Moves the asteroid certain spaces at a certain speed and sets its coordinates accordingly 
        """
        if self.__x > 0:
            self.__x -= 3
        self.__canvas.coords(self.__asteroid, self.__x, self.__y)
        self.__mId = self.__canvas.after(self.__speed, self.move)
        
    def showBlast(self):
        """Cancels the movement of the asteroid and shows the blast image and then deletes the asteroid
        """
        self.stopMovement()
        self.__canvas.itemconfig(self.__asteroid, image = self.__imgblast[self.__value])
        self.__canvas.after(1000, self.delete)

    def delete(self):
        """Deletes the current asteroid
        """
        self.__canvas.delete(self.__asteroid)
        
    def stopMovement(self):
        """Stops the movement of the asteroid
        """
        self.__canvas.after_cancel(self.__mId)
