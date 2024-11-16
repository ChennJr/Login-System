import tkinter as tk
from tkinter.messagebox import showinfo
credentials = []

root = tk.Tk() # Create the root window
root.geometry("300x150") # Set the dimensions of the window
root.resizable(False, False) # Disable resizing the window  
root.title("Login") # Set the title of the window
username_input = tk.StringVar() 
password_input = tk.StringVar() 
switch_frame = False

with open("credentials.txt", "r") as file:
    data = file.readlines()
    for line in data:
        credentials.append(line.split())

class chooseGame():
    def __init__(self, game):
        self.game_choice = game
    
    def run_game(self):
        if self.game_choice == "snake":
            exec(open("Snake.py").read(), globals())

        elif self.game_choice == "dice":
            print("Dice Game")

class signIn:
    def __init__(self):
        self.sign_in = tk.Frame(root)
        self.sign_in.pack(padx=10, pady=10, fill='x', expand=True)
        self.switch_frame = False
        
        self.username_label = tk.Label(self.sign_in, text="Username:", anchor='w') # Create a username label widget
        self.username_entry = tk.Entry(self.sign_in, textvariable = username_input) # Create a username entry widget

        self.password_label = tk.Label(self.sign_in, text="Password:", anchor='w') # Create a password label widget
        self.password_entry = tk.Entry(self.sign_in, textvariable=password_input, show="*",) # Create a password entry widget

        self.button = tk.Button(self.sign_in, text="Enter", command=self.account_search) # Create an enter button widget
        self.show_password_button = tk.Button(self.sign_in, text="Show", command=self.toggle_show_password, height=1,width=5) # Create a show password button widget
    
    def pack_widgets(self):
        self.username_label.pack(fill='x', expand=True)
        self.username_entry.pack(fill='x', expand=True)
        self.username_entry.focus()

        self.password_label.pack(fill='x', expand=True)
        self.password_entry.pack(fill='x', expand=True,) 

        self.button.pack(side = 'left', fill='x', expand=True, padx=1, pady=5) 
        self.show_password_button.pack(side='left', fill='x', padx=1, pady=5)

    def account_search(self):
        for x in range(len(credentials)):
            if password_input.get() == str(credentials[x][1])  and username_input.get() == str(credentials[x][0]):
                msg = "Account found"
                self.sign_in.pack_forget()
                music = Page()
                music.pack_widgets()

                return showinfo(title="Searching", message=msg)
            
            else:
                pass
        
        msg = "Account not found"
        return showinfo(title="Searching", message=msg)
            
    def toggle_show_password(self):
        if signIn.password_entry.cget('show') == "":
            signIn.password_entry.config(show="*")
            signIn.show_password_button.config(text="Show")
    
        else:
            signIn.password_entry.config(show="")
            signIn.show_password_button.config(text="Hide")



class Page:
    def __init__(self):
        self.page = tk.Frame(root)
        self.page.pack(padx=10, pady=10, fill='x', expand=True)
        
        snake_game = chooseGame("snake")
        dice_game = chooseGame("dice")

        self.snake_button = tk.Button(self.page, text="Play Snake", command=snake_game.run_game) # Create a play snake button widget
        self.dice_game_button = tk.Button(self.page, text="Play Dice Game", command=dice_game.run_game) # Create a play dice game button widget


    def pack_widgets(self):
        self.snake_button.pack(side = 'top', fill='x', expand=True)
        self.dice_game_button.pack(side = 'top', fill='x', expand=True)


signIn = signIn()

if signIn.switch_frame == False:
    signIn.pack_widgets()


root.mainloop()


