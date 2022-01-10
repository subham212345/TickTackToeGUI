import tkinter.messagebox
from tkinter import *

# Creating the window with white background and giving it the title: Tick Tack Toe
window = Tk()
window.title("Tick Tack Toe")
window.configure(background="white")


message = tkinter.messagebox

# Player1 begins from "X"
mouse_click = True
count = 0
winner = False


# Disable buttons
def disable_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)


# Check who won
def check_win():
    global winner
    # Conditions for when player1(X) won
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="green")
        button2.config(bg="green")
        button3.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button4["text"] == "X" and button6["text"] == "X" and button5["text"] == "X":
        button6.config(bg="green")
        button4.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="green")
        button8.config(bg="green")
        button9.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="green")
        button5.config(bg="green")
        button9.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button7.config(bg="green")
        button3.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button7.config(bg="green")
        button1.config(bg="green")
        button4.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="green")
        button8.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button9.config(bg="green")
        button3.config(bg="green")
        button6.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player1 has won")
        disable_buttons()


    # Conditions for when player2(O) won
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="green")
        button2.config(bg="green")
        button3.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button4["text"] == "O" and button6["text"] == "O" and button5["text"] == "O":
        button6.config(bg="green")
        button4.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="green")
        button8.config(bg="green")
        button9.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="green")
        button5.config(bg="green")
        button9.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button7.config(bg="green")
        button3.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button7.config(bg="green")
        button1.config(bg="green")
        button4.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="green")
        button8.config(bg="green")
        button5.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button9.config(bg="green")
        button3.config(bg="green")
        button6.config(bg="green")
        winner = True
        message.showinfo("Tick Tack Toe", "Player2 has won")
        disable_buttons()
    elif count == 9 and winner == False:
        message.showinfo("Tick Tack Toe", "It is a tie!!")
        disable_buttons()



# Creating the button click
def button_click(button):
    global mouse_click, count

    if button["text"] == "" and mouse_click == True:
        button["text"] = "X"
        mouse_click = False
        count += 1
    elif button["text"] == "" and mouse_click == False:
        button["text"] = "O"
        mouse_click = True
        count += 1
    else:
        message.showerror("Tick Tack Toe", "The box has already been selected.\n Please select another box")
    check_win()


# Building the buttons
# Start/ Rest the game
def reset():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global  mouse_click, count
    mouse_click = True
    count = 0
    button1 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button1))
    button2 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button2))
    button3 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button3))

    button4 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button4))
    button5 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button5))
    button6 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button6))

    button7 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button7))
    button8 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button8))
    button9 = Button(window, text="", font=("arial", 20, "bold"), height=6, width=6,
                         bg="White", fg="black", command=lambda: button_click(button9))

    # Placing the buttons on grid
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)


# Create menu
menu = Menu(window)
window.config(menu=menu)

# Create options for menu
options = Menu(menu, tearoff=False)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=reset)

reset()
window.mainloop()
