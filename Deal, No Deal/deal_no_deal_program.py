#Name: Richelle Pereira
#Date: 14/10/2020
#Course Code: ICS4U1-01
#Program Name: Deal or No Deal 

#Import module with following elements and functions
from tkinter import Tk, Frame, Label, PhotoImage, Button, messagebox
import random
import math

# Function which shows leaving message before user exiting the program
def exit_window():
    messagebox.showinfo("Game Over","Thank you for playing Deal or No Deal!" )
    root.destroy()
def quit_window():
    ans = messagebox.askyesno("Deal or No Deal","Are you sure you want to quit?" )
    if ans == True:
        messagebox.showinfo("Deal or No Deal","Thank you for playing Deal or No Deal!" )
        root.destroy()

# Function asks the user and resets the program to play again accordingly 
def play_again():
    option = messagebox.askyesno("Deal or No Deal","Would you like to play again?")
    # If above statement is true then reset program, else close the window
    if option == True:
        create_reset()
        pass
    else:
        exit_window()

# Function initializes variables, creates money labels and buttons with their hidden shuffled amounts
def create_reset():
    global x, round_num, count, amounts
    #Initialize the following variables
    x = 0
    round_num = 1
    count = calc_round(round_num)
    # Code clears the data within the lists and sets all lists and labels states
    selected_cases.clear()
    our_case.clear()
    amounts.clear()
    amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    lblPlayersCase.config(image = imgPlayersCase )
    lblMessage.config(text = "Choose one of the briefcases!")

    # Code configures the labels for the users to see and gives it the corresponding amount
    for i in range(len(lbl_money)):
                    lbl_money[i][0].config(image = imgMoney[i])
                    lbl_money[i][1] = amounts[i]
    
    #Code shuffles the amounts list and creates the buttons and assigns the shuffled amount to a case
    random.shuffle(amounts)
    counter = 0
    #Code creates 5 rows with 1st 4 rows having 5 columns and last row having 6 columns ands sets a random amount to each case
    for rows in range(len(btnCases)):
        for cols in range(len(btnCases[rows])):
            if rows <= 3:
                btnCases[rows][cols] = Button(centerframe, bg = "black", bd = 0, image = imgCases[counter], command = lambda row = rows, col = cols, amount = amounts[counter], case_num = counter, lbl_num = counter: check_selection(row, col, amount, case_num, lbl_num))
            else:
                btnCases[rows][cols] = Button(bttmframe, bg = "black", bd = 0, image = imgCases[counter], command = lambda row = rows, col = cols, amount = amounts[counter], case_num = counter, lbl_num = counter: check_selection(row, col, amount, case_num, lbl_num))
            btnCases[rows][cols].grid(row = rows, column = cols, pady = 4, padx = 4)
            counter +=1

#Function formats the decimal to the proper rounding place
def format_decimal(number, deci_place):
    decimal=  math.floor(number * 100 + 0.5)/100
    return decimal

#Function calculates according to the round number how many cases should be selected each round
def calc_round(round_num):
    global lblMessage
    if round_num == 1:
        count = 6
    elif round_num == 2:
        count = 5
    elif round_num == 3:
        count = 4
    elif round_num == 4:
        count = 3
    elif round_num == 5:
        count = 2
    else:
        count = 1
    return count

#Function gets the index of the amount in the 2d list
def get_index(amount):
        for x, a in enumerate(lbl_money):
                for y, b in enumerate(a):
                        if b == amount:
                                index = x
        return index

# Function calculates the banker's offer to the user after each round by calculating average amount of money left, multiplied by round number, divided by 10
def bank_offer(round_num):
        total = 0
        for i in range(len(amounts)):
                total += amounts[i]
        avg_money = float(total / (len(amounts)))
        # Offer equals to the average of the remaining money amounts multiplied by the round number divided by 10
        offer = float(avg_money*round_num/10)
        num = format_decimal(offer, 2) 
        return num

#Initialize following list and variables
x = 0
round_num = 1
count = calc_round(round_num)
selected_cases = []
our_case = []

# Function checks the user's case option and removes the money labels and calculates accordingly
def check_selection(row, col, amount, case_num, lbl_num):
        global x, round_num, count
        #Statement checks if value of x is 0, if true, it stores the 1st case as the player's chosen case
        if x == 0:
                # Code stores the 1st selected case and does the following
                our_case.append([btnCases[row][col], amount])
                lblPlayersCase.config(image = (btnCases[row][col].cget("image")))
                btnCases[row][col].config(image = imgBlankCase, state = "disabled")
                lblMessage.config(text = "Open 6 briefcase(s)")
                x += 1
        # If statement not true, following code removes the amount labels selected according to each round after the 1st case is stored
        else:
                # Loop reveals the amount in that case and removes the case and its amount label 
                while count != 0:
                        # Code stores all the selected cases and their revealed amounts and does the following
                        selected_cases.append([btnCases[row][col], amount])
                        messagebox.showinfo("Case #"+str(case_num+1), "Case #"+str(case_num+1)+" contains $ "+ "{:,}".format(amount)+"!" )
                        lblMessage.config(text = "Open "+str(count-1)+" briefcase(s)")
                        btnCases[row][col].config(image = imgBlankCase, state = "disabled")
                        amounts.remove(amount)
                        index = get_index(amount)
                        lbl_money[index][0].config(image = imgBlankMoney)
                        count -=1
                        break
                # Statement checks if the all the cases for that round are opened, if true then program calculates and gives a bank offer to accept or reject 
                if count == 0:
                                offer = bank_offer(round_num)
                                ans = messagebox.askyesno("Banker's Offer", "The banker's offer is $ "+ "{:,.2f}".format(offer) +"\nWould you like to take the deal?")
                                #Statement checks if the user takes the offer, if true, then goes home with the offer and is asked a prompt
                                if ans == True:
                                        messagebox.showinfo("It's a deal!", "Congratulations...you're going home with $ "+ "{:,.2f}".format(offer)+"!")
                                        messagebox.showinfo("Deal or No Deal", "You could've gone home with $ "+ "{:,.2f}".format(our_case[0][1])+".")
                                        play_again()
                                # If user doesn't take the offer, the program continues with the rounds and revealing the cases
                                else:
                                    round_num +=1
                                    count = calc_round(round_num)
                                    lblMessage.config(text = "Open "+str(count)+" briefcase(s)")
                                    # Statement checks if the selected cases are 24, meaning when all the cases are revealed except the user's case and one another, if true then program asks user the following and performs accordingly   
                                    if len(selected_cases) == 24:
                                            choice = messagebox.askyesno("Deal or No Deal", "There is only one case left! \nWould you like to keep your case?")
                                            # Statement checks if the user wants to swap cases with the last case
                                            if choice == False:
                                                # If the user decides to swap their case then, user gets the amount in the other case
                                                amounts.remove(our_case[0][1])
                                                messagebox.showinfo("Deal or No Deal", "Congratulations...you're going home with $ "+ "{:,.2f}".format(amounts[0])+".")
                                                play_again()
                                            else:
                                                # if the user decides to keep their case then, user gets the amount in their originally selected case
                                                messagebox.showinfo("Deal or No Deal", "Congratulations...you're going home with $ "+ "{:,.2f}".format(our_case[0][1])+".")
                                                play_again()
                                            
# Creates a window and main frame and set properties                
root = Tk()
root.title("Deal or No Deal")
root.protocol("WM_DELETE_WINDOW", quit_window)
frame = Frame(root, padx=10, pady=10, bg="black")
frame.pack()
# Creates the label for the title and set its properties and image
imgTitle = PhotoImage(file="images/dond_logo.png")
lblTitle = Label(frame, image=imgTitle, border=0)
lblTitle.grid(row=0, column=0, columnspan=3)
# Creates the label for the extra money bag and set its properties and image
bag_img = PhotoImage(file= "images/moneybag.png")
lblimg = Label(frame, image = bag_img, border =0, bg = "black")
lblimg.grid(row = 2, column = 2, padx= 5, pady = 5)

# Creates frames for the labels and cases for the user to see and sets its properties
westframe = Frame(frame, padx=10, pady=10, bg="black")
westframe.grid(row=1, column=0)
eastframe = Frame(frame, padx=10, pady=10, bg="black")
eastframe.grid(row=1, column=2)
centerframe = Frame(frame, padx=20, pady=10, bg="black", width=380, height=280)
centerframe.grid(row=1, column=1)
bttmframe = Frame(centerframe, bg = "black")
bttmframe.grid(row = 5, column = 0, columnspan = 6, sticky = "w")

# Creates label for the message
lblMessage = Label(frame, width=35, bg="black", font=("Century Gothic", 14, "bold"), fg="#fcea97", text="Choose one of the briefcases!")
lblMessage.grid(row=2, column=1, padx=10, pady=5)

# Initializes variables to the images and list to images of the numbered suitcases and images of the amount labels
imgBlankCase = PhotoImage(file="images/suitcases/blankcase.png")
imgBlankMoney = PhotoImage(file = "images/money/blankmoney.png")
imgCases = (PhotoImage(file = "images/suitcases/case1.png"),PhotoImage(file = "images/suitcases/case2.png"), PhotoImage(file = "images/suitcases/case3.png"), PhotoImage(file = "images/suitcases/case4.png"), PhotoImage(file = "images/suitcases/case5.png"),
            PhotoImage(file = "images/suitcases/case6.png"),PhotoImage(file = "images/suitcases/case7.png"), PhotoImage(file = "images/suitcases/case8.png"),PhotoImage(file = "images/suitcases/case9.png"), PhotoImage(file = "images/suitcases/case10.png"),
            PhotoImage(file = "images/suitcases/case11.png"),PhotoImage(file = "images/suitcases/case12.png"), PhotoImage(file = "images/suitcases/case13.png"),PhotoImage(file = "images/suitcases/case14.png"), PhotoImage(file = "images/suitcases/case15.png"),
            PhotoImage(file = "images/suitcases/case16.png"),PhotoImage(file = "images/suitcases/case17.png"), PhotoImage(file = "images/suitcases/case18.png"), PhotoImage(file = "images/suitcases/case19.png"), PhotoImage(file = "images/suitcases/case20.png"),
            PhotoImage(file = "images/suitcases/case21.png"),PhotoImage(file = "images/suitcases/case22.png"), PhotoImage(file = "images/suitcases/case23.png"), PhotoImage(file = "images/suitcases/case24.png"), PhotoImage(file = "images/suitcases/case25.png"), PhotoImage(file = "images/suitcases/case26.png"))
imgMoney = (PhotoImage(file = "images/money/0.01.png"), PhotoImage(file = "images/money/1.png"), PhotoImage(file = "images/money/5.png"),PhotoImage(file = "images/money/10.png"),PhotoImage(file = "images/money/25.png"),PhotoImage(file = "images/money/50.png"),PhotoImage(file = "images/money/75.png"),
            PhotoImage(file = "images/money/100.png"), PhotoImage(file = "images/money/200.png"),PhotoImage(file = "images/money/300.png"), PhotoImage(file = "images/money/400.png"),PhotoImage(file = "images/money/500.png"),PhotoImage(file = "images/money/750.png"),PhotoImage(file = "images/money/1000.png"),
            PhotoImage(file = "images/money/5000.png"), PhotoImage(file = "images/money/10000.png"),PhotoImage(file = "images/money/25000.png"),PhotoImage(file = "images/money/50000.png"),PhotoImage(file = "images/money/75000.png"),PhotoImage(file = "images/money/100000.png"),PhotoImage(file = "images/money/200000.png"),
            PhotoImage(file = "images/money/300000.png"), PhotoImage(file = "images/money/400000.png"),PhotoImage(file = "images/money/500000.png"),PhotoImage(file = "images/money/750000.png"),PhotoImage(file = "images/money/1000000.png"))

# Creates a 2d list for the labels for amount images to be stored in
lbl_money = [[0 for x in range(2)] for y in range(26)]

# Creates the player's case label and sets the properties
imgPlayersCase = imgBlankCase
lblPlayersCase = Label(frame, image=imgPlayersCase, bg="black")
lblPlayersCase.grid(row=2, column=0)

# Creates jagged list for the cases 
numcols = [5, 5, 5, 5, 6]
btnCases = [[] for j in range(len(numcols))]
for i in range (len(btnCases)):
    btnCases[i] = [0]*numcols[i]
#Initializes the list with the money amounts 
amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

# Creates the labels for the money amounts and stores them in the lbl money list
for i in range(len(lbl_money)):
            #Statement checks if i is smaller then or equal to 12, if true then labels are created and are placed to the westframe
            if i <= 12:
                    lbl_money[i][0] = Label(westframe, image = imgMoney[i], bg = "black")
                    lbl_money[i][0].grid(row = i+1, column = 0, pady = 3, padx = 5)
            #if i is greater then 12, then labels are created and placed on the eastframe 
            else:
                    lbl_money[i][0]= Label(eastframe, image = imgMoney[i], bg = "black")
                    lbl_money[i][0].grid(row = i+1, column = 3, pady = 3, padx = 5)
            lbl_money[i][1] = amounts[i]
                    
create_reset()
# Execute the program
root.mainloop()
