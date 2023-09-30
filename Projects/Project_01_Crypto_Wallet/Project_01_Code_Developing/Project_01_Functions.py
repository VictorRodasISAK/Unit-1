with open("../Project_01_Files/Project_01_Words1.csv", mode="r") as words_file:
    words = words_file.readlines()

def uname_repeated(uname: str) -> bool:
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    success = False
    for line in data:
        user = line.split(',')[0].strip()
        if user == uname:
            success = True
            break
    return success


def validate_pass(upass:str) -> bool:
    upper, lower, num = False, False, False
    count = 0
    for letter in upass:
        count += 1
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True
        elif letter.isnumeric():
            num = True
    if count < 7:
        return False

    return upper and lower and num


def try_login(msg1: str, msg2: str) -> bool:
    name = input(msg1)
    pass_login = input(msg2)
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    success = False
    for line in data:
        user = line.split(',')[0]
        upass = line.split(',')[1].strip()
        if user == name and upass == pass_login:
            success = True
            break
    return success


def recover_password(msg1: str, msg2: str, msg3: str, msg4: str, msg5: str) -> str:
    user_val = input(msg1)
    q1 = input(msg2).lower()
    q2 = input(msg3).lower()
    q3 = input(msg4).lower()
    q4 = input(msg5).lower()
    with open('../Project_01_Files/Project_01_Users_Logged.csv', mode='r') as f:
        data = f.readlines()
    show_password = ""
    for line in data:
        line_user = line.strip().split(",")
        user_correct = line_user[0].strip()
        if user_correct == user_val:
            ques1, ques2, ques3, ques4 = line_user[2], line_user[3], line_user[4], line_user[5]
            if ques1 == q1 and ques2 == q2 and ques3 == q3 and ques4 == q4:
                show_password += f"{words[19]}{line_user[1]}\n{words[20]}"
                break
            else:
                show_password += f"{words[59]}"
    return show_password


def frame_maker(msg: str, sym: str, space: int, num:int) -> str:
    if num == 1:
        x = "\33[0;30m" #Black
    elif num == 2:
        x = "\33[0;31m" #Red
    elif num == 3:
        x = "\33[0;32m" #Green
    elif num == 4:
        x = "\33[0;33m" #Yellow
    elif num == 5:
        x = "\33[0;34m" #Blue
    elif num == 6:
        x = "\33[0;35m" #Purple
    elif num == 7:
        x = "\33[0;36m" #Cyan
    elif num == 8:
        x = "\33[0;37m" #White
    width = 2 + 2 * space + len(msg)
    end_code = "\033[00m"

    top_line = sym * width
    middle_line = sym + " "*(width-2) + sym
    msg_line = sym + " "*space + msg.upper() + " "*space + sym

    banner = f"{x}{top_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{top_line}{end_code}"
    return banner

def valid_number(msg: str, valid: str) -> str:
    valid_num = input(msg)
    while not valid_num in valid:
        print("ERROR!")
        valid_num = input(msg)
    return valid_num

def valid_value(msg: str) -> float:
    amount = input(msg)
    temp1 = amount.replace(".", "")
    while not temp1.isnumeric():
        amount = input(words[40])
        temp1 = amount.replace(".", "")
    withdraw_amount = float(amount)
    return withdraw_amount

def date_comparison(msg: str) -> str:
    while True:
        date_search = input(msg)
        splits_date = date_search.split("-")
        if len(splits_date) == 3:
            year, month, day = splits_date
            if day.isdigit() and month.isdigit() and year.isdigit():
                year, month, day = int(year), int(month), int(day)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    date = f"{year}-{month:02}-{day:02}"
                    return date

        print(words[48].strip())

def reason_transaction(list:list) -> str:
    print(words[54].strip())
    print(words[56])
    for word in range(len(list)):
        print(f"{word+1}. {list[word]}\n".strip())
    print()
    reason = valid_number(msg=words[55], valid="12345")
    return list[int(reason) - 1]


def project_leave():
    print(words[35].strip())
    print(words[36])
    number = valid_number(msg=words[3], valid="12")
    if number == '1':
        return words[37]
    elif number == "2":
        print(frame_maker(msg=words[52].strip(), sym="*", space=50, num=5))
    return exit(1)
