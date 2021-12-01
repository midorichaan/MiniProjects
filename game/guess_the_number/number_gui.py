import random
import sys
import Tkinter

root = Tkinter.Tk()
number = 0
is_playing = False
count = 0

def generate_number():
    return random.randint(000, 999)

def setup_root():
    global root
    root.title(u"Guess The Number")
    root.geometry("400×300")
    
    label = Tkinter.Label(
        text=u"Enter the number (000 - 999)", 
    )
    label.pack()
    
    box = Tkinter.Entry()
    box.pack()

def run():
    global is_playing, count, number
    
    
    while is_playing == True:
        
        
if __name__ == "__main__":
    try:
        setup_root()
        root.mainloop()
        run()
    except Exception as exc:
        print(f"[Error] {exc}")
