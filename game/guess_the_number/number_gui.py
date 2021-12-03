import random
import sys
import tkinter
import tkinter.font as font

root = tkinter.Tk()
number = 0
count = 0
font = font.Font(root, family="無心", size=20)

box = None
button = None
label = None
counter = None
hint = None
close = None

def generate_number():
    return random.randint(000, 999)

def on_button_click():
    global count, counter

    n = box.get()
    print(f"Button Clicked: Value - {n}")
    box.delete(0, tkinter.END)

    if not n.isdigit():
        print("value is not number")
        return

    n = int(n)
    count += 1
    counter["text"] = u"挑戦回数: {}".format(count)

    if n > number:
        print("lower")
    elif n < number:
        print("higher")
    else:
        print("collect")
        print(f"The answer is {number} (trying {count} times)")

def setup_root():
    global root, box, button, label, close, counter, hint
    root.title(u"数当てゲーム")
    root.geometry("400x150")
    
    label = tkinter.Label(
        text=u"3桁の数字を入力してください", 
        font=font
    )
    label.place(
        x=75, 
        y=15
    )

    counter = tkinter.Label(
        text=u"挑戦回数: {}".format(count),
        font=font
    )
    counter.place(
        x=140,
        y=40
    )
    
    hint = tkinter.Label(
        text=u"debug",
        font=font
    )
    hint.place(
        x=180,
        y=70
    )

    box = tkinter.Entry(width=20)
    box.place(
        x=110, 
        y=70
    )
    
    button = tkinter.Button(
        text=u"入力",
        font=font,
        command=on_button_click
    )
    button.place(
        x=120, 
        y=100
    )

    close = tkinter.Button(
        text=u"終了",
        font=font,
        command=root.destroy
    )

    close.place(
        x=200,
        y=100
    )        
        
if __name__ == "__main__":
    try:
        setup_root()
        number = generate_number()
        root.mainloop()
    except Exception as exc:
        root.quit()
        print(f"[Error] {exc}")
