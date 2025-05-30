import tkinter as tk
from tkinter import messagebox
import random
import time

def center_window(window):
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (500 // 2)
    y = (window.winfo_screenheight() // 2) - (300 // 2)
    window.geometry(f'500x300+{x}+{y}')

def move_no_button(event):
    global attempts, no_button, counter_label, question_label, subtitle, window
    attempts += 1
    counter_label.config(text=f'Pathetic attempts: {attempts}')
    
    max_x = 500 - 120
    max_y = 300 - 50
    
    speed_mult = min(attempts // 3 + 1, 5)
    for i in range(speed_mult):
        x = random.randint(0, max_x)
        y = random.randint(60, max_y)
        no_button.place(x=x, y=y)
        window.update()
        time.sleep(0.05)
    
    roast_user()

def roast_user():
    global attempts, no_button, question_label, subtitle, window, counter_label
    
    if attempts <= 5:
        msgs = ["Nah", "Nope", "Try harder", "Not today"]
        no_button.config(text=random.choice(msgs))
        
    elif attempts <= 11:
        msgs = ["Still no", "Keep trying champ", "This is sad", "Really?"]
        no_button.config(text=random.choice(msgs))
        question_label.config(text="Seriously? Still trying?")
        
    elif attempts <= 24:
        msgs = ["I'm programmed to hate you", "System says no", "404: Dignity not found", "Error: Desperation overflow"]
        no_button.config(text=random.choice(msgs))
        question_label.config(text="This is actually embarrassing")
        subtitle.config(text="(Your persistence is concerning)")
        
    elif attempts <= 36:
        msgs = ["I'm calling the police", "This is harassment", "Stop. Please.", "I have a restraining order"]
        no_button.config(text=random.choice(msgs))
        question_label.config(text="DUDE. STOP.")
        subtitle.config(text="(Seriously, this is getting weird)")
        window.configure(bg='#330000')
        question_label.configure(bg='#330000')
        subtitle.configure(bg='#330000')
        counter_label.configure(bg='#330000')
        
    else:
        msgs = ["I'm dead inside", "You broke me", "System.exe has stopped", "Why are we still here?", "Just to suffer?"]
        no_button.config(text=random.choice(msgs))
        question_label.config(text="You've broken the system")
        subtitle.config(text="(Congratulations, psychopath)")
        window.configure(bg='#000000')
        question_label.configure(bg='#000000', fg='#ff0000')
        subtitle.configure(bg='#000000', fg='#ff0000')
        counter_label.configure(bg='#000000', fg='#ff0000')
        
        if attempts > 50:
            no_button.config(text="I give up", state='disabled', bg='#666666')
            yes_button.config(text="You monster", bg='#ff0000')

def yes_clicked():
    global attempts
    
    if attempts == 0:
        msgs = [
            "Wow. You didn't even try to resist.\nThat's... actually concerning.",
            "Well that was easy.\nDo you have any self-respect?",
            "Congratulations!\nYou're exactly as predictable as I thought.",
            "Amazing! You chose the rigged option!\nGenius level: 0"
        ]
    elif attempts < 25:
        msgs = [
            f"Only {attempts} attempts? Weak.\nI expected more fight from you.",
            f"After {attempts} tries you gave up?\nPathetic but expected.",
            f"{attempts} attempts and you surrender?\nAt least you know when you're beaten."
        ]
    elif attempts < 40:
        msgs = [
            f"After {attempts} attempts you finally cracked.\nI respect the persistence, not the outcome.",
            f"{attempts} tries? Not bad.\nStill chose the obvious answer though.",
            f"Took you {attempts} attempts to accept the inevitable.\nSlow learner, huh?"
        ]
    else:
        msgs = [
            f"AFTER {attempts} ATTEMPTS?!\nYou're either very determined or very stupid.",
            f"{attempts} tries and you STILL clicked yes?\nI don't know whether to be impressed or concerned.",
            f"You tried {attempts} times and gave up?\nThat's the most beautiful tragedy I've ever seen."
        ]
    
    messagebox.showinfo("Victory(?)", random.choice(msgs))
    
    play_again = messagebox.askyesno("One Last Thing", "Want to play again?\n(So I can roast you some more?)")
    
    if play_again:
        window.destroy()
        playi()
    else:
        messagebox.showinfo("Goodbye", "Smart choice.\nFor once.")
        window.quit()

def playi():
    global window, question_label, subtitle, yes_button, no_button, counter_label, attempts
    
    attempts = 0
    
    window = tk.Tk()
    window.geometry('500x300')
    window.title('Definitely Not Manipulation')
    window.configure(bg='#1a1a1a')
    window.resizable(False, False)
    
    center_window(window)
    
    question_label = tk.Label(
        window, 
        text='Do you like me?', 
        font=('Courier', 18, 'bold'),
        bg='#1a1a1a',
        fg='#00ff00'
    )
    question_label.pack(pady=40)
    
    subtitle = tk.Label(
        window,
        text='(This is totally a fair choice)',
        font=('Courier', 10),
        bg='#1a1a1a',
        fg='#666666'
    )
    subtitle.pack()
    
    yes_button = tk.Button(
        window,
        text='Obviously Yes',
        font=('Arial', 12, 'bold'),
        bg='#ff6b6b',
        fg='white',
        padx=20,
        pady=10,
        cursor='hand2',
        command=yes_clicked
    )
    yes_button.place(x=80, y=150)
    
    no_button = tk.Button(
        window,
        text='No (Good luck)',
        font=('Arial', 10),
        bg='#4ecdc4',
        fg='white',
        padx=15,
        pady=8,
        cursor='crosshair'
    )
    no_button.place(x=280, y=155)
    no_button.bind('<Enter>', move_no_button)
    no_button.bind('<Button-1>', move_no_button)
    no_button.bind('<Motion>', move_no_button)
    
    counter_label = tk.Label(
        window,
        text='Escape attempts: 0',
        font=('Courier', 9),
        bg='#1a1a1a',
        fg='#ffff00'
    )
    counter_label.place(x=10, y=270)
    
    window.mainloop()

playi()
