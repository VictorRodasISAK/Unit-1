def frame_maker(msg: str, sym: str, space: int) -> str:
    height = 5
    width = 2 + 2 * space + len(msg)
    red = "\33[0;31m"
    end_code = "\033[00m"

    top_line = sym * width
    middle_line = sym + " "*(width-2) + sym
    msg_line = sym + " "*space + msg.upper() + " "*space + sym

    banner = f"{top_line}\n{middle_line}\n{red}{msg_line}{end_code}\n{middle_line}\n{top_line}"
    return banner

title = "Welcome to Conbini"
cover_game = frame_maker(msg=title, sym="y", space=40)
print(cover_game)

logo = """
             ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-'     conbini
"""

print(logo)
x = "MENU".center(50, " ")
print(x)

with open("Untitled spreadsheet - Sheet1.csv", "r") as myfile:
    database = myfile.readlines()

items = []
prices = []
for line in database:
    line = line.strip()
    name, price = line.split(",")
    items.append(name)
    prices.append(int(price))

for it in range(len(items)):
    print(f"{it + 1}. {items[it].title().ljust(50, '.')}¥{prices[it]}")

order = []
ordering = True
total = 0
while ordering:
    selection = input(f"Please enter an item (1-{len(items)}): ")
    available = ""
    for i in range(len(items)):
        available += str(i + 1)

    while not (selection.isdigit() and selection in available):
        selection = input(f"Please enter an item (1-{len(items)}): ")

    order.append(int(selection) - 1)
    total += prices[int(selection) - 1]

    for it in range(len(items)):
        count = 0
        for o in order:
            if o == it:
                count += 1
        if count > 0:
            total_price = prices[it]*count
            print(f"{items[it].title().ljust(20)}x{count} = ¥{total_price}")

    answer = input("Is this the last item? (Y/N) ")
    while not answer in "yYnN":
        answer = input("Error. Last item?(Y/N) ")

    if answer in "yY":
        ordering = False

print(frame_maker(msg=f"You need to pay ¥{(total*1.1):.2f}", space=50, sym="$"))

with open("Cool_Game_Sales.csv", "a") as myfile:
    myfile.writelines(f"order date total {(total * 1.1):.2f}\n")

"""
items = ['onigiri', 'bread', 'chips']
prices = [500, 200, 150]

for it in range(len(items)):
    print(f"{it + 1}. {items[it].title().ljust(50, '.')}¥{prices[it]}")

order = []
ordering = True
total = 0
while ordering:
    selection = input(f"Please enter an item (1-{len(items)}): ")
    available = ""
    for i in range(len(items)):
        available += str(i + 1)

    while not (selection.isdigit() and selection in available):
        selection = input(f"Please enter an item (1-{len(items)}): ")

    order.append(int(selection) - 1)
    total += prices[int(selection) - 1]

    for it in range(len(items)):
        count = 0
        for o in order:
            if o == it:
                count += 1
        if count > 0:
            total_price = prices[it]*count
            print(f"{items[it].title().ljust(20)}x{count} = ¥{total_price}")

    answer = input("Is this the last item? (Y/N) ")
    while not answer in "yYnN":
        answer = input("Error. Last item?(Y/N) ")

    if answer in "yY":
        ordering = False

print(frame_maker(msg=f"You need to pay ¥{(total*1.1):.2f}", space=50, sym="$")) """