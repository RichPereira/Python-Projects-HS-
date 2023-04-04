from tkinter import Tk, Frame, Button, Label, PhotoImage, messagebox
import random


counter, minutes, seconds, startgame, timer_id = 0, 0, 0, False, None

def run_timer():
    global seconds, minutes, timer_id
    timer_id = root.after(1000, run_timer)
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    lblStart .config(text = str(minutes)+ ":"+ "{:0>2d}".format(seconds))

def start_game():
    global minutes, seconds, startgame, timer_id
    if startgame == False:
        random.shuffle(imgmovies)
        
        for rows in range(len(btnMovies)):
            for cols in range(len(btnMovies[rows])):
                btnMovies[rows][cols].config(image = imgblank)
                btnMovies[rows][cols].config(state = "normal")

        lblStart .config(text = str(minutes)+ ":"+ "{:0>2d}".format(seconds))
        run_timer()
        btnStart.config(text = "STOP")
        startgame = True
    else:
        root.after_cancel(timer_id)
        btnStart.config(text = "START")
        startgame = False
    
def exit_program():
    answer = messagebox.askyesno("Memory Game", "Are you sure you want to quit?")
    if answer == True:
        root.destroy()

def button_click(row, col, picid):
    global counter, minutes, seconds
    btns_selected[counter]= btnMovies[row][col]
    counter += 1
    btnMovies[row][col].config(image = imgmovies[picid])
    imgs = 17

    if counter == 2:
        if btns_selected[0].cget("image") == btns_selected[1].cget("image"):
            messagebox.showinfo("Memory Game", "You have found a match")
            btns_selected[0].config(state = "disabled")
            btns_selected [1].config(state = "disabled")
            counter = 0
        else:
            messagebox.showinfo("Memory Game", "No match")
            btns_selected[0].config(image = imgblank, state = "normal")
            btns_selected [1].config(image = imgblank, state = "normal")
            counter = 0

    for rows in range(len(btnMovies)):
        for cols in range(len(btnMovies[rows])):
            if btnMovies[rows][cols].cget("state") == "disabled":
                imgs -= 1
                if imgs == 0:
                    start_game()
                    ans = messagebox.showinfo("Memory Game", "Congratulations! You cleared the board in "+ str(minutes)+ ":"+ "{:0>2d}".format(seconds)+ ". \nWould you like to play again?")
                    minutes, seconds = 0, 0
            else:
                pass
root = Tk()
root.title("Memory Game")
root.protocol("WM_DELETE_WINDOW", exit_program)

frame = Frame(root, padx=10, pady=10)
frame.pack()

lblTitle = Label(frame, text="MEMORY GAME", font=("Britannic Bold", 24)).grid(row=0, column=0, pady=10, columnspan=6)
lblStart = Label(frame, text="Click START to begin!", font=("Britannic Bold", 18))
lblStart.grid(row=4, column=0, columnspan=6, pady=10)
btnStart = Button(frame, text="START", width=70, font=("Britannic Bold", 14), command = start_game)
btnStart.grid(row=5, column=0, columnspan=6, pady=10)

imgmovies = [PhotoImage(file="images/annabelle.png"), PhotoImage(file="images/gone_girl.png"), PhotoImage(file="images/interstellar.png"), 
    PhotoImage(file="images/the_equalizer.png"), PhotoImage(file="images/the_maze_runner.png"), PhotoImage(file="images/transformers.png"), 
    PhotoImage(file="images/walk_among_tombstones.png"), PhotoImage(file="images/dracula_untold.png"), PhotoImage(file="images/guardians_of_galaxy.png")]

btns_selected = [0]* 2

imgmovies += imgmovies
imgblank = PhotoImage(file="images/blank.png")

btnMovies  = [[0 for cols in range(6)] for rows in range(3)]
picindex = 0 
for rows in range(len(btnMovies)):
    for cols in range(len(btnMovies[rows])):
        btnMovies[rows][cols] = Button(frame, image = imgblank, state = "disabled", command = lambda picid=picindex , row = rows, col = cols: button_click(row, col, picid))
        btnMovies[rows][cols].grid(row = rows+1, column = cols, pady = 5)
        picindex += 1



root.mainloop()
