import random
def color(num: object) -> object:
    if num == 1:
        x = "\33[0;30m"
    elif num == 2:
        x = "\33[0;31m"
    elif num == 3:
        x = "\33[0;32m"
    elif num == 4:
        x = "\33[0;33m"
    elif num == 5:
        x = "\33[0;34m"
    else:
        print("The value entered is not correct")
    return x

color_num = color(num= 3)
def frame_maker(msg: str, sym: str, space: int) -> str:
    height = 5
    width = 2 + 2*space + len(msg)
    end_code = "\033[00m"

    top_line = sym * width
    middle_line = sym + " "*(width-2) + sym
    msg_line = sym + " "*space + msg.upper() + " "*space + sym

    banner = f"{top_line}\n{middle_line}\n{color_num}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

title = "A cool game"
cover_game = frame_maker(msg=title, sym="y", space=40)
print(cover_game)


secret_number = random.randint(1, 101)
count = 0
x = int(input("Please enter a guess "))
while x != secret_number:
    if x > secret_number:
        print("Too big")
    else:
        print("Too small")
    x = int(input("Please enter a guess "))
    count +=1

print(f"You won, it took you {count + 1} tries")
