# Name: Richelle Pereira
# Date: 24/10/2020
# Course Code: ICS4U1-01
# Program: Baccarat Card Game


# Import the following modules
from tkinter import Tk, Canvas, PhotoImage, Entry, Button, END, INSERT, Frame, messagebox
from DeckOfCards import DeckOfCards
from Player import Player

# Function asks the user if they want to quit and does according to the user's answer
def exit_window():
    ans = messagebox.askyesno("Baccarat", "Are you sure you want to exit?")
    if ans == True:
        root.destroy()
    else:
        pass
    
# Function displays the 3rd card for the player and does changes the scores
def playerDrawCard():
    global banker_score
    canvas.itemconfig(img_playerCards[2], image = player.getCards(2).getImage())
    player_score, banker_score = player.playerScore(), banker.playerScore()
    canvas.itemconfig(outputPlayer, text = str(player_score)), canvas.itemconfig(outputBanker, text = str(banker_score))
    checkWinner(player_score, banker_score)
    
# Function draws 3rd card only for the banker and changes the score and checks the winner    
def bankerDrawCard():
    global player_score
    # Deals the card for the banker and shows the cards for the player and banker
    banker.dealCards(2) , canvas.itemconfig(img_bankerCards[2], image = banker.getCards(2).getImage()), canvas.itemconfig(img_playerCards[2], image = player.getCards(2).getImage())
    banker_score, player_score = banker.playerScore(), player.playerScore()
    canvas.itemconfig(outputPlayer, text = str(player_score)), canvas.itemconfig(outputBanker, text = str(banker_score))
    checkWinner(player_score, banker_score)

# Function checks the winner after dealing the cards and adds, subtracts points accordingly
def checkWinner(player_score, banker_score):
    global chiptotal
    btnDeal.config(command = deal_card)
    # Statement checks if the player score is greater than banker score, if true then the inputed bet amount is added to chip total and output message
    if player_score > banker_score:
        chiptotal += int(entryBet.get())
        canvas.itemconfig(outputMessage, text = "Player WON!!") 
    # Statement checks if the player score is < banker score, if true the then the inputed bet amount is subtracted from the chip total and output message
    if player_score < banker_score:
        chiptotal -= int(entryBet.get())
        canvas.itemconfig(outputMessage, text = "Banker WON!!")
    # Statement checks if both scores are = to each other, if true, output message
    if player_score == banker_score:
        canvas.itemconfig(outputMessage, text = "Both Players TIED!!")
        
    canvas.itemconfig(outputChips, text ="$" + "{:,d}".format(chiptotal)), btnBet.config(state = "normal"),btnDeal.config(text= "DEAL",state = "disabled"), entryBet.config(state = "normal")
    
    # Statement checks if the chip total equals 0 if true as the user to play again
    if chiptotal == 0:
        ans = messagebox.askyesno("Baccarat", "Game over! You have $0 remaining. \nWould you like to play again?")
        if ans == True:
            # If true, program is reset
            chiptotal = 500
            btnDeal.config(text= "DEAL",state = "disabled"), entryBet.delete(0, END), canvas.itemconfig(outputChips, text = "$" + "{:,d}".format(chiptotal) )
            reset_create()
        else:
            # Else, program closes
            root.destroy()
            
# Function checks if the inputed valued for the bet is valid    
def take_bet():
    global chiptotal, deck
    # Checks if the value inputed is an integer
    try:
        # Statement checks if the value is an integer
        if int(entryBet.get()) == int(entryBet.get()):
            # Then checks if the values is greater than the chiptotal and also if it is less than or equal to 0, if true then shows message
            if int(entryBet.get()) > chiptotal:
                messagebox.showerror("Error", "Your bet cannot exceed $"+ str(chiptotal)+"!")
            elif int(entryBet.get()) <= 0:
                messagebox.showerror("Error", "You must bet at least $1!")
            else:
                # If above not true, change state of the buttons
                btnDeal.config(text = "DEAL", state = "normal"), btnBet.config(state = "disabled"), canvas.itemconfig(outputMessage, text = "Click DEAL!"), entryBet.config(state = "readonly", readonlybackground = "white")
    # If not,  shows the following message
    except ValueError: 
        messagebox.showinfo("Error", "You must enter an integer!")  

# Function deals 2 cards to each player and calculates if to draw the 3rd card
def deal_card():
    reset_create()
    # Code deals 2 cards to both players and sets the image according to their draw 
    player.dealCards(0), player.dealCards(1), banker.dealCards(0), banker.dealCards(1)
    canvas.itemconfig(img_playerCards[0], image = player.getCards(0).getImage()), canvas.itemconfig(img_playerCards[1], image = player.getCards(1).getImage())
    canvas.itemconfig(img_bankerCards[0], image = banker.getCards(0).getImage()), canvas.itemconfig(img_bankerCards[1], image = banker.getCards(1).getImage())
    # Scores of both players are calculated and set the variables after cards are dealt, also displayed to the user on the canvas
    player_score, banker_score  = player.playerScore(), banker.playerScore()
    canvas.itemconfig(outputPlayer, text = str(player_score)), canvas.itemconfig(outputBanker, text = str(banker_score))
    
    # Statement check if the player score or banker score is 8 or 9  
    if player_score == 8 or player_score == 9 or banker_score == 8 or banker_score == 9:
        # If true, then check the winner
        checkWinner(player_score, banker_score)
    else:
        # Statement check if the player score is 6 or 7
        if player_score == 6 or player_score == 7:
            # If true, then checks if the banker score equals 5 or less
            if banker_score <= 5:
                # If true, banker draws card and output message
                btnDeal.config(text= "DRAW CARD", command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            else:
                # Else, check winner
                checkWinner(player_score, banker_score)
        # Statement check if player score is less than or equal to 5
        elif player_score <= 5:
            # If true then player draws card
            canvas.itemconfig(outputMessage, text = "Draw one more card!"), btnDeal.config(text = "DRAW CARD")
            player.dealCards(2), canvas.itemconfig(img_playerCards[2], img = imgBlank)
            player_score = player.playerScore()
            # Statement check if the banker score is 0, 1, 2, if true, banker draws
            if banker_score == 0 or banker_score == 1 or banker_score == 2:
                btnDeal.config(command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            # Statement checks if the banker score is 3 and player score is not 8, if banker draws
            elif banker_score == 3 and player_score != 8:
                btnDeal.config(command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            # Statement checks if the banker score is 4 and player score is between 2-7, if true, banker draws
            elif banker_score == 4 and (player_score >=2 and player_score <= 7):
                btnDeal.config(command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            # Statement checks if the banker score is 5 and player score is between 4-7, if true, banker draws
            elif banker_score == 5 and (player_score >=4 and player_score <= 7):
                btnDeal.config(command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            # Statement checks if the banker score is 6 and player score is 6 or 7, if true, banker draws
            elif banker_score == 6 and (player_score == 6 or player_score == 7):
                btnDeal.config(command = bankerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            # Statement checks if the banker score is 7 after the player draws 3rd card, only player draws
            elif banker_score == 7:
                btnDeal.config(command = playerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
            else:
                # If above statements are not true do, do the following
                btnDeal.config(command = playerDrawCard), canvas.itemconfig(outputMessage, text = "Draw one more card!")
                            
# Function creates card, player, deck objects and outputs the images of the cards created
def reset_create():
    global deck, player, banker, img_playerCards, img_bankerCards
    # Initialize/create the following objects
    deck = DeckOfCards()
    player, banker = Player(deck), Player(deck)
    # Creates/outputs the images of the cards for both players
    img_playerCards = [canvas.create_image(250, 210, image = player.getCards(0).getImage()), canvas.create_image(250, 270, image = player.getCards(1).getImage()), canvas.create_image(250, 330, image = player.getCards(2).getImage())]
    img_bankerCards = [canvas.create_image(550, 210, image = banker.getCards(0).getImage()), canvas.create_image(550, 270, image = banker.getCards(1).getImage()), canvas.create_image(550, 330, image = banker.getCards(2).getImage())]
    canvas.itemconfig(outputMessage, text="Place BET to begin"), canvas.itemconfig(outputPlayer, text = "0"), canvas.itemconfig(outputBanker, text = "0")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------


WINDOW_WIDTH, WINDOW_HEIGHT = 800, 534
# Creates the main window and canvas and sets its properties
root = Tk()
root.title("Baccarat")
root.geometry("%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, root.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2, root.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2))

canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Creates the following images and outputs the title on the canvas
imgbackground, imgBlank,imgtitle  = PhotoImage(file="images/card_table.png"), PhotoImage(file = "images/back_blue.png"), PhotoImage(file="images/baccarat.png")
canvas.create_image(0, 0, image=imgbackground, anchor='nw') 
canvas.create_image(WINDOW_WIDTH // 2 - imgtitle.width() // 2, 10, image=imgtitle, anchor='nw')

canvas.create_text(250, 425, text='Player has:', font=('Century Gothic', 14, 'bold'), fill='white'), canvas.create_text(550, 425, text='Banker has:', font=('Century Gothic', 14, 'bold'), fill='white')

# Creates/outputs the message, banker score, player score on the canvas
outputMessage = canvas.create_text(WINDOW_WIDTH // 2, 385, text="Place BET to begin", font=('Century Gothic', 12, 'bold'), fill='white')
outputPlayer = canvas.create_text(250, 455, text='0', font=('Century Gothic', 14, 'bold'), fill='white')
outputBanker = canvas.create_text(550, 455, text='0', font=('Century Gothic', 14, 'bold'), fill='white')

reset_create()
chiptotal = 500
outputChips = canvas.create_text(WINDOW_WIDTH // 2, 160, font=('Century Gothic', 28, 'bold'), fill='white', text="$" + "{:,d}".format(chiptotal))
# Creates the frame and the entry and sets its properties
frame = Frame(root, borderwidth=2, relief='sunken')
entryBet = Entry(frame, width=12, font=('Century Gothic', 10, 'bold'), justify='center', borderwidth=5, relief='flat')
entryBet.insert(INSERT, '0'), entryBet.focus(), entryBet.selection_range(0, END)
entryBet.pack()
root.update()
frame.place(x=WINDOW_WIDTH // 2 - frame.winfo_reqwidth() // 2, y=190)

# Creates buttons and sets the properties 
btnBet = Button(canvas, width=13, text='PLACE BET', pady=5, command = take_bet)
btnBet.place(x=WINDOW_WIDTH // 2 - btnBet.winfo_reqwidth() // 2, y=235)
btnDeal = Button(canvas, width=13, text='DEAL', pady=5, state='disabled', command = deal_card)
btnDeal.place(x=WINDOW_WIDTH // 2 - btnDeal.winfo_reqwidth() // 2, y= 280)
btnQuit = Button(canvas, width=13, text='QUIT', pady=5, command = exit_window)
btnQuit.place(x=WINDOW_WIDTH // 2 - btnQuit.winfo_reqwidth() // 2, y = 325)

# Execute the program
root.mainloop()