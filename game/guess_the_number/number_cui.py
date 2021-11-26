import random

number = 0
is_playing = False

def generate_number():
    return random.randint(000, 999)

def run():
    global number, is_playing
    number = generate_number()
    is_playing = True

    while is_playing == True:
        i = input("Enter the number (000 〜 999) > ")
        
        if not i.isdigit():
            print("number must be a integer")
            continue
        
        i = int(i)

        if number > i:
            print("higher")
        elif number < i:
            print("lower")
        else:
            print(f"collect! answer is {number}")
            is_playing = False
    print("Game ended.")

if __name__ == "__main__":
    run()
