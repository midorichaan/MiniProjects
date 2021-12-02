import random
import sys
import tkinter
import tkinter.font as font

root = tkinter.Tk()
box = None
number = 0
button = None
label = None
is_playing = False
count = 0
font = font.Font(root, family="./mushin.otf", size=20)

def generate_number():
    return random.randint(000, 999)

def setup_root():
    global root, box, button, count, label
    root.title(u"Guess The Number")
    root.geometry("400x150")
    
    label = tkinter.Label(
        text=u"Enter the number (000 - 999) [{}]".format(count), 
        font=font
    )
    label.place(
        x=20, 
        y=20
    )
    
    box = tkinter.Entry(width=10)
    box.place(
        x=110, 
        y=55
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
