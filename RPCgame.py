import tkinter as tk
import random
from PIL import Image, ImageTk 

#creating the window space
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("550x400")
window.resizable(width="false",height="false")
window.configure(bg="lightblue")
#initializing the images icons
rock_img = ImageTk.PhotoImage(Image.open("ROCK.jpg").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("PAPER.jpg").resize((100,100)))
scissors_img = ImageTk.PhotoImage(Image.open("SCISSORS.jpg").resize((100,100)))

moves = ["rock","paper","scissors"]
#creating the function
def game(user_choice):
    computer_choice = random.choice(moves)
    result = ""
    
    if user_choice == computer_choice :
        result = "TIE"
    elif (user_choice == "rock" and computer_choice == "scissors") or\
         (user_choice == "paper" and computer_choice == "rock") or\
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "YOU WIN"
    else:
        result = "YOU LOSE"
    
    result_lab.config(text = f"You chose: {user_choice} and the computer chose:{computer_choice}\nTherefore : {result}")
#main program

#creating the frames for the execution
main_Frame = tk.Frame(window,bg="white",highlightbackground="black",highlightthickness="2")
main = tk.Label(main_Frame,text="Choose ROCK,PAPER or SCISSORS",font=('Arial Black',10,'bold'),bg="white")
main.pack(pady=10)
side_frame = tk.Frame(main_Frame,highlightbackground="black",highlightthickness="2")
#creating the buttons
Rock_btn = tk.Button(side_frame,image = rock_img,command =lambda: game("rock"),bg="blue")
paper_btn = tk.Button(side_frame,image = paper_img,command= lambda: game("paper"),bg="red")
scissors_btn = tk.Button(side_frame,image=scissors_img,command= lambda: game("scissors"),bg="yellow")
#structuring the layout
Rock_btn.grid(row=0,column=0,padx=5,pady=5)
paper_btn.grid(row=0,column=1,padx=5,pady=5)
scissors_btn.grid(row=0,column=2,padx=5,pady=5)
side_frame.pack(padx=5,pady=5)
#result label
result_lab = tk.Label(main_Frame, text = "",font=('Consolas' ,10,'bold'),bg="white",anchor="center",justify="center")
result_lab.pack()
main_Frame.pack(padx=10,pady=70,ipadx=10,ipady=10)

window.mainloop()