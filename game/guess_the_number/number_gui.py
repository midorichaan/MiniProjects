import random
import sys
import tkinter
import tkinter.font as font

root = tkinter.Tk()
box = None
number = 0
button = None
is_playing = False
count = 0
font = font.Font(root, family="./mushin.otf", size=20, weight="bold")

def generate_number():
    return random.randint(000, 999)

def setup_root():
    global root, box, button
    root.title(u"Guess The Number")
    root.geometry("400×150")
    
    label = tkinter.Label(
        text=u"Enter the number (000 - 999)", 
        font=font
    )
    label.place(
        x=20, 
        y=20
    )
    
    box = tkinter.Entry()
    box.place(
        width=4, 
        x=120, 
        y=60
    )
    
    button = tkinter.Button(
        text=u"入力",
        font=font
    )
    button.place(x=120, y=100)

def run():
    global is_playing, count, number
    
    number = generate_number()
    is_playing = True
    
    while is_playing == True:
        is_playing = False
        
if __name__ == "__main__":
    try:
        setup_root()
        root.mainloop()
        run()
    except Exception as exc:
        print(f"[Error] {exc}")
