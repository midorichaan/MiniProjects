import random

number = 0
count = 0
is_playing = False

def generate_number():
    return random.randint(000, 999)

def run():
    global number, is_playing, count
    
    number = generate_number()
    is_playing = True

    while is_playing == True:
        try:
            i = input("Enter the number [{count}] (000 〜 999) > ")
        except:
            is_playing = False
        
        if not i.isdigit():
            print("number must be a integer")
            continue
        
        i = int(i)
        count += 1

        if number > i:
            print("higher")
        elif number < i:
            print("lower")
        else:
            print(f"collect! answer is {number} ({count})")
            is_playing = False
    print("Game ended.")

if __name__ == "__main__":
    run()
