#Name: Richelle Pereira
#Date: 1/11/2020
#Course Code: ICS4U-01
#Program: Asterpocalypse - Space Shooter Program


#Import the following modules and packages
from tkinter import Tk, Canvas, PhotoImage, messagebox
from Spaceship import Spaceship
from Bullet import Bullet
from Asteroid import Asteroid
import pygame

#Function stops the background timer and window is destroyed
def exit_program():
    root.after_cancel(btid)
    root.destroy()

#Function moves the background after every 50 millisecond
def background_timer():
    global btid
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5
    btid = root.after(50, lambda: background_timer())
    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

#Function fires a bullet each time space bar is clicked
def onkeypress(event):
    #Statement check id space bar key is pressed
    if event.keysym == "space":
        #If true, bullet is created and fired
        b = Bullet(canvas)
        b.setLocation((ship.getX() + ship.getWidth()), (ship.getY() + ship.getHeight()//2))
        pygame.mixer.Sound.play(laserSound)
        b.fireBullet()
        #Statement checks if the bullet touches the end of the window
        if b.getX() + b.getWidth() > canvas.winfo_reqwidth():
            #if true, then bullet is deleted from the list
            b.deleteBullet()
            bullet.remove(b)
        #If not true, the pass
        else:
            pass
        bullet.append(b)

#Function sets the position of the ship to the mouse position on the canvas
def onmousemove(event):
    #Sets the position of the mouse to the sip
    ship.setLocation((event.x - ship.getWidth()//2), (event.y - ship.getHeight()//2))
    #Statements checks if the ship is in the canvas and not off screen, if yes then re-sets the position of the ship
    if event.x < 50:
        ship.setLocation(0, ship.getY())
    if event.x > 955:
        ship.setLocation(canvas.winfo_reqwidth() - ship.getWidth(), ship.getY())
    if event.y < 75:
        ship.setLocation(ship.getX(),56)
    if event.y > 535:
        ship.setLocation(ship.getX(),510)

#Function checks collision of the asteroid and the end screen, asteroid and the ship, asteroid and the bullet and executes the corresponding code
def checkCollision():
    global small, medium, large, points, asteroid_id, btid, lives, health, lives, ship
    #Code checks the collision every millisecond
    collision_id = root.after(1, checkCollision)

    for a in asteroid:
        #Statement checks if the asteroid's x position is less than 0
        if a.getX() < 0:
            #If true, then remove the asteroid from the list and subtract and update health bar
            a.delete(), asteroid.remove(a)
            health-=1
            canvas.itemconfig(health_bar, image = img_health[health])
            #Statement checks if the health is -1
            if health == -1:
                #If true, life is lost each time and health is restored to normal
                lives -= 1
                health = 10
                canvas.itemconfig(showlives, image = img_lives[lives]), canvas.itemconfig(health_bar, image = img_health[health])
                #Statement checks if the lives equal to 0
                if lives == 0:
                    #If true, then code stops movement of all asteroids and cancels all timers and outputs message
                    canvas.itemconfig(health_bar, image = img_health[0])
                    for a in asteroid:
                        a.stopMovement()
                        root.after_cancel(collision_id), root.after_cancel(btid), root.after_cancel(asteroid_id)
                        checkLives()
        else:
            pass
    
    for a in asteroid:
        #Statement checks if the ship touches the asteroid in terms of their positions and widths and heights
        if ship.getX() + ship.getWidth() - 4 >= a.getX() - a.getWidth() + 4 and ship.getX() + 4 <= a.getX() -4:  
            if ship.getY() + ship.getHeight()-4 >= a.getY() +4 and ship.getY() +4 <= a.getY() + a.getHeight() -4:
                #If true, then background music is paused and ship explodes
                pygame.mixer.music.pause()
                pygame.mixer.Sound.play(shipBlast), ship.explode(), canvas.itemconfig(health_bar, image = img_health[0])
                #All timers are canceled 
                root.after_cancel(collision_id), root.after_cancel(btid), root.after_cancel(asteroid_id)
                #Code stops movement of all the asteroids
                for a in asteroid:
                    a.stopMovement()
                #Player loses a life and then is updated    
                lives -= 1
                canvas.itemconfig(showlives, image = img_lives[lives])
                #Statement checks if the lives don't equal to 0
                if lives != 0:
                    #If true, then following message is shown
                    messagebox.showinfo("Asterpocalypse", "You're dead!\n You have "+ str(lives) + " lives remaining!")
                    #Health variable is reset to full
                    health = 10
                    canvas.itemconfig(health_bar, image = img_health[health])
                    #Ship is deleted and re-initialized, asteroid list is cleared and timers are reset
                    canvas.delete(ship)
                    ship = Spaceship(canvas, x = 45, y = imgBackground.height()//2)
                    asteroid.clear() ,pygame.mixer.music.unpause(),resetTimers()
                #If lives equal to 0, then does the following
                else:
                    checkLives()

    for b in bullet:
        for a in asteroid:
            #Statement check  if the bullet touches the asteroid in terms of their positions and widths and heights
            if b.getX() + b.getWidth()>=  a.getX() - a.getWidth() +30 and b.getX()<= a.getX() + a.getWidth()-5:
                if b.getY() + b.getHeight()>=  a.getY() and b.getY()<= a.getY() + a.getHeight()-5:
                    #If above statement true, bullet disappears, is removed from list and then is reset
                    b.deleteBullet(), bullet.remove(b), b.reset()
                    # Checks if the asteroid hit is a small asteroid 
                    if a.getWidth() == 52:
                        small -= 1
                        #Statement checks if user hit the asteroid 1 times, if true, then shows the blast and adds points and removes the asteroid from list
                        if small == 0:
                            pygame.mixer.Sound.play(blast),a.showBlast()
                            points += 10
                            canvas.itemconfig(score, text = str(points))
                            small = 1
                            asteroid.remove(a)
                            break
                    #Checks if the asteroid hit is a medium asteroid         
                    if a.getWidth() == 80:
                        medium -= 1
                        #Statement checks if user hit the asteroid 2 times, if true, then shows the blast and adds points and removes the asteroid from list
                        if medium == 0:
                            pygame.mixer.Sound.play(blast), a.showBlast()
                            points += 20
                            canvas.itemconfig(score, text = str(points))
                            medium = 2
                            asteroid.remove(a)
                            break                             
                    # Checks if the asteroid hit is a large asteroid         
                    if a.getWidth() == 160:
                        large -= 1
                        #Statement checks if user hit the asteroid 3 times, if true, then shows the blast and adds points and removes the asteroid from list
                        if large == 0:
                            pygame.mixer.Sound.play(blast), a.showBlast()
                            points += 30
                            canvas.itemconfig(score, text = str(points))
                            large = 3
                            asteroid.remove(a)
                            break

#Function checks if lives equal 0 and asks user to play again or exit and depending on the choice, program quits or resets  
def checkLives():
    global lives, points
    pygame.mixer.music.stop()
    ans = messagebox.askyesno("Asterpocalypse", "GAME OVER! \n You have finished the game with " + str(points)+ " points. \n Would you like to play again?")
    if ans == True:
        create_resetGame()
    else:
        asteroid.clear(), root.destroy()

#Function initializes the following variables and start the timers and background music 
def create_resetGame():
    global small, medium, large, health, points, lives, ship, score, health_bar, showlives, time
    canvas.itemconfig(score, text = "0"), canvas.itemconfig(health_bar,image = img_health[10]), canvas.itemconfig(showlives, image = img_lives[3])
    canvas.delete(ship), asteroid.clear(), bullet.clear()
    small, medium, large = 1, 2, 3
    health, points, lives = 10, 0, 3
    time = 0
    ship = Spaceship(canvas, x = 45, y = imgBackground.height()//2)
    pygame.mixer.music.play(-1), resetTimers()

#Function creates an asteroid at a time interval and then as time passes creates many asteroids and stores them in a list
def createAsteroid():
    global asteroid_id, time
    asteroid.append(Asteroid(canvas, speed = 15))
    if time <= 15:
        asteroid_id = root.after(2000, createAsteroid)
    elif time > 15 and time <= 30:
        asteroid_id = root.after(1250, createAsteroid)
    elif time > 30:
        asteroid_id = root.after(850, createAsteroid)
    time +=2 
    

#Function calls to start all the game timers
def resetTimers():
    createAsteroid(), checkCollision(), background_timer()
      
      
# Create the main window
root = Tk()
root.title('Asterpocalypse')
root.protocol('WM_DELETE_WINDOW', exit_program)
#Create images for background
imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')
#Set window properties
root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2, root.winfo_screenheight() // 2 - imgBackground.height() // 2))
root.bind("<Motion>", onmousemove)
root.bind("<KeyPress>", onkeypress)
#Create canvas and set properties
canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()
#Initializes the background list
background_list = [0] * 2
xpos = [0, imgBackground.width()]
#Creates the background for the window
for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')
#Creates the health images
img_health = [0]* 11
for i in range(len(img_health)):
    img_health[i] = PhotoImage(file = "images/health"+ str(i) + ".png")
#Creates life images and stores them in a list
img_lives = ["", PhotoImage(file = "images/lives1.png"), PhotoImage(file = "images/lives2.png"), PhotoImage(file = "images/lives3.png")]

#Canvas, creates and shows  the title image, score, health bar, and lives on the window and sets properties
canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')
score = canvas.create_text(120,35, fill = "gold", font = ("Neuropol",25,"bold"), text = "0")
health_bar = canvas.create_image(canvas.winfo_reqwidth() - img_health[10].width() + 45 , 15, image = img_health[10])
showlives = canvas.create_image(canvas.winfo_reqwidth() - img_lives[3].width()+ 29, 42, image = img_lives[3])

#Initializes the mixer
pygame.mixer.init()
# Initializes the variables with their sounds
blast = pygame.mixer.Sound("explosion.wav")
laserSound = pygame.mixer.Sound("laserSound.wav")
shipBlast =  pygame.mixer.Sound("shipblastSound.wav")
pygame.mixer.music.load("boss.ogg")

#Creates the lists and spaceship
asteroid = []
bullet = [] 
ship = Spaceship(canvas, x = 45, y = imgBackground.height()//2)
create_resetGame()
# Executes the entire program
root.mainloop()
