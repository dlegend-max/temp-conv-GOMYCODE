import tkinter as tk
import random
from PIL import Image, ImageTk 

#creating the window space
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("600x450")
window.resizable(width="false",height="false")
window.configure(bg="lightblue")
#initializing the images icons
rock_img = ImageTk.PhotoImage(Image.open("ROCK.jpg").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("PAPER.jpg").resize((100,100)))
scissors_img = ImageTk.PhotoImage(Image.open("SCISSORS.jpg").resize((100,100)))

moves = ["rock","paper","scissors"]
user_score = 0
comp_score = 0
max_round = 5
round = 1
#creating the function
def game(user_choice):
    global user_score,comp_score,round
    if round > max_round :
         score_label.config(text="Game over! Click 'Restart' to play again.")
         return

    computer_choice = random.choice(moves)
    result = ""
   
        
    if user_choice == computer_choice :
        result = "TIE"
        
    elif (user_choice == "rock" and computer_choice == "scissors") or\
         (user_choice == "paper" and computer_choice == "rock") or\
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "YOU WIN"
        user_score += 1
    else:
        result = "YOU LOSE"
        comp_score += 1
   
    
    result_lab.config(text = f"You chose: {user_choice} and the computer chose:{computer_choice}\nTherefore : {result} this round")
    score_label.config(text = f" ROUND {round} \n YOUR SCORE : {user_score} | COMPUTER SCORE: {comp_score}")
    round += 1
    
    if round > max_round:
        if user_score > comp_score:
            final = "YOU WIN THIS GAME!"
        elif user_score == comp_score:
            final = "YOU DREW THIS GAME!"
        else:
            final = "YOU LOSE THIS GAME!"
        result_lab.config(text=result_lab.cget("text") + f"\n\n{final}")
def restart():
    global user_score, comp_score, round
    user_score = 0
    comp_score = 0
    round = 1
    score_label.config(text="YOUR SCORE: 0 | COMPUTER SCORE: 0")
    result_lab.config(text="Choose a move to start the game of 5 rounds.")
#main program

#creating the frames for the execution
main_Frame = tk.Frame(window,bg="white",highlightbackground="black",highlightthickness="2")
main = tk.Label(main_Frame,text="Choose ROCK,PAPER or SCISSORS",font=('Arial Black',10,'bold'),bg="white")
main.pack(pady=10)
side_frame = tk.Frame(main_Frame,highlightbackground="black",highlightthickness="2")
#creating the buttons
Rock_btn = tk.Button(side_frame,image = rock_img,text="rock",command =lambda: game("rock"),bg="blue")
paper_btn = tk.Button(side_frame,image = paper_img,command= lambda: game("paper"),bg="red")
scissors_btn = tk.Button(side_frame,image=scissors_img,command= lambda: game("scissors"),bg="yellow")
#structuring the layout
Rock_btn.grid(row=0,column=0,padx=5,pady=5)
paper_btn.grid(row=0,column=1,padx=5,pady=5)
scissors_btn.grid(row=0,column=2,padx=5,pady=5)
side_frame.pack(padx=5,pady=5)
#result label
result_lab = tk.Label(main_Frame, text = "Choose a move to start the game of 5 rounds",
                      font=('Consolas' ,10,'bold'),bg="white",anchor="center",justify="center")
result_lab.pack()
main_Frame.pack(padx=10,pady=30,ipadx=10,ipady=10) 


score_frame =tk.Frame(window,bg="white",highlightbackground="black",highlightthickness="2",width=100,height=40)
score_label = tk.Label(score_frame,text = f"ROUNDS:",bg = "white")
score_label.pack(ipady=5)
restart_btn = tk.Button(score_frame,text= "restart",command=restart)
restart_btn.pack(pady=5)
score_frame.pack(ipadx=3,ipady=3)

window.mainloop()