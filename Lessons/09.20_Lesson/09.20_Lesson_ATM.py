import datetime

from Lesson_Library import frame_maker, print_menu, validate_integer

msg = frame_maker(msg= "Welcome to ATM", sym="$", space=50)
print(msg)

menu = ["Deposit","Withdraw", "Balance", "Show Bar Graph"]
print("The menu is: ")
print_menu(menu)


option = 5
while option not in [1, 2, 3, 4]:
    option = validate_integer(msg="Please enter an option ", menu=menu)


option = int(option)
if option == 1:
    amount = validate_integer(msg="Please enter amount to deposit: ", menu= "")
    date = datetime.date.today()
    line = f"{date},{amount}\n"
    with open('09.20_ATM_File.csv', mode='a') as f:
        f.writelines(line)
    print("Saved")

if option == 3:
    with open('09.20_ATM_File.csv', mode='r') as f:
        data = f.readlines()
    balance = 0
    for line in data:
        date, amount = line.strip().split(',')
        balance += int(amount)
    today = datetime.date.today()
    msg = f"Your balance {today} is ¥{balance}"
    print(frame_maker(msg= msg, sym= '$', space= 50))

if option == 4:
    with open('09.20_ATM_File.csv', mode='r') as f:
        data = f.readlines()
    deposits = 0
    withdraws = 0
    for line in data:
        date, amount = line.strip().split(',')
        if int(amount) > 0:
            deposits += int(amount)
        else:
            withdraws += -1 * int(amount)


    deposits = deposits // 100
    withdraws = withdraws // 100
    bar_deposits = "Deposits".ljust(20)
    bar_withdraws = "Withdraws".ljust(20)
    for x in range(deposits):
        bar_deposits += "▥"
    for x in range(withdraws):
        bar_withdraws += "▥"

    print(f"{bar_deposits} {deposits}")
    print(f"{bar_withdraws} {withdraws}")